#!/bin/bash
#rev date 2011-02-17 (insilicoscientist@gmail.com)
#~~~~"Glide VSW HTVS, SP, XP dock energy data extractor"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~EnsembleVS_dataAnalyzer-v1_20110217.sh 2011-02-17, insilicoscientist@gmail.com~~~~~~~~~~~
#~~~~The input file for this script is the CSV format output from Glide VSW jobs~~~~~~~~~~~~~~

export ROOT_DIR=$(pwd)

DIR0="VS_Shelf"
#Directory for VS energy outout
DIR1="VS_DockEnergyOutput"
#Directory for enrichment calculation result outout
DIR2="VS_EnrichmentCalcOutput"
#Dock Pose output files copied to this directory
DIR3="VS_DockPoseOutput"
#Directory for RMSD calculation 
DIR4="VS_RMSDCalcOutput"
#Temporary work directory
DIR5="VS_TempWorkDir"

#Actives file.
a=validationLib_actives_30_39_20110205.maegz

#Number of decoys/inactives
b=76

#Docked pose RMSD calculation native ligand conformation reference file
RMSD_REF_POSE_FILE="validationLib_set1_actives_knownConf_native_16_20110204.mae"

#VSW Job name prefixes with a '-'
#If all HTVS, SP and XP are run in a same vsw job script, all of the values will be same
J1="vsw_01_HTVS-"
J2="vsw_01_SP-"
J2="vsw_01_XP-"

#################################################################################################
function vs_dee {
#VS Data Extraction begins here
echo "VS Data Extraction begins"
echo "Current working directory:"
pwd
echo "Checking for the result data output directory:"
echo $ROOT_DIR/$DIR1

if [[ ! -d "$DIR1" ]];
then
    mkdir $DIR1
    echo "VS Dock energy result data output directory $DIR1 created"
else
    echo "VS Dock energy result data output directory $DIR1 already exists."
    echo "Deleting $DIR1"
    rm -rf $DIR1
    mkdir $DIR1
    echo "VS Dock energy result data output directory $DIR1 created"
fi

#First, create a name list of docking jobs for each ensemble. 
pwd
ls -al | grep 'drwx' | grep "\-DOCK_" | awk '{print $8}' > dock.list

#Read each of the job name from the list and loop over. The variable x is the job name.
for x in `cat dock.list` 
 do
	cd $x
	echo 'Extracting data for job' $x
	y=`ls 2>/dev/null *_pv.maegz *lib.maegz | sed -e 's/_pv.maegz//' -e 's/_lib.maegz//'| tail -1`
	#If you have any values with ',', that would give incorrect column delimitting. 
	#Read the raw data from .CSV and replace the wrong value with correct one using sed and output new file
	sed -e 's/"143_Akt-I-1,2"/143_Akt-I-1-2/g' -e 's/"143_Akt-I-1,2-1"/143_Akt-I-1-2/g' < $y.csv >$x.data

	#echo 'Reading the header (first line of CSV) and asigning the column number'
	#Read the header (first line of CSV) and asign the column number to a variable
	TITLE_FIELD=`head -1 $x.data | awk -F, '{for(i=1;i<=NF;i=i+1) {if ($i=="s_m_title")print i} }'`
	DOCKINGSCORE_FIELD=`head -1 $x.data | awk -F, '{for(i=1;i<=NF;i=i+1) {if ($i=="r_i_docking_score")print i} }'`

	#Now extract the two columns using awk and store it in a temporary file
	awk -v p="$TITLE_FIELD" -v q="$DOCKINGSCORE_FIELD" -F, '{print $p","$q}' <$x.data >$x.dock.energy.temp-list1

	#Add ranking to the table, assuming that the docking result is sorted by docking score. 
	#First value is '0'. The output is stored as another temporary files
	nl -s, -v 0 $x.dock.energy.temp-list1 > $x.dock.energy.temp-list2

	#Get a short word to replace the CSV titles. 
	#Helpful to uniquely identify when merging all data together.
	TITLE_FLAG="`echo $x | awk -F'DOCK_' '{ print $2 }'`"

	#Now replace the title with that short word and delete the whitespaces
	sed "s/r_i_docking_score/"$TITLE_FLAG""_E"/g" <$x.dock.energy.temp-list2 >$x.dock.energy.temp-list3
	sed "s/\s0\,/"$TITLE_FLAG""_R,"/g" <$x.dock.energy.temp-list3 >$x.dock.energy.temp-list4
	sed 's/s_m_title/s_user_newID/g' <$x.dock.energy.temp-list4 >$x.dock.energy.temp-list5
	sed 's/ //g' <$x.dock.energy.temp-list5 >$x.dock.energy.list
	
	#Move the final file to a directory, DIR1 one level up
	mv $x.dock.energy.list $ROOT_DIR/$DIR1/$x.dock.energy.csv

	#Remove all the temporary files; Comment this if you need to check any errors by retaining the intermediate files
	rm -f *temp-list*
	rm -f $x.data
	
	echo 'Job for' $x 'completed'
	#Go up one level and loop over to the next job
	cd ..
 done

#Merging the all the VS data to a single CSV file which can be imported to the maestro project table
#MayaChemTools "MergeTextFiles.pl" perlscript is used in the process

cd $DIR1

k=`ls | wc -l`
l=s_user_newID # For -k flag for the program; The unique key for merging the files
for (( i=1; i<$k; i++ ))
do
	l=`echo $l";s_user_newID"`
done

../$DIR0/MergeTextFiles.pl -r Merged_EnsembleVS_Energies.csv -k "$l" -m collabel -o *.csv

echo 'Each of the VS docking energy is merged into "Merged_EnsembleVS_Energies.csv" file'
echo 'VS Data Extraction finished'
cd ..
#VS Data Extraction ends here
}
#################################################################################################
#################################################################################################
function vs_en {
#VS Enrichment calculation begins here
echo "VS Enrichment calculation begins"
echo "Current working directory:"
pwd
echo "Checking for the VS Enrichment result data output directory $DIR2 in:"
pwd

if [[ ! -d "$DIR2" ]];
 then
    mkdir $DIR2
    echo "VS Enrichment Result data output directory $DIR2 created"
 else
    echo "VS Enrichment Result data output directory $DIR2 already exists."
    echo "Deleting $DIR2"
    rm -rf $DIR2
    mkdir $DIR2
    echo "VS Enrichment Result data output directory $DIR2 created"
fi

if [[ ! -d "$DIR3" ]];
 then
    mkdir $DIR3
    echo "Dock pose output directory $DIR3 created"
 else
    echo "Dock pose output directory $DIR3 already exists."
    echo "Deleting $DIR3"
    rm -rf $DIR3
    mkdir $DIR3
    echo "Dock pose output directory $DIR3 created"
 fi

if [[ ! -d "$DIR5" ]];
 then
    mkdir $DIR5
    echo "Temporary work directory $DIR5 created"
 else
    echo "Temporary work directory $DIR5 already exists."
    echo "Deleting $DIR5"
    rm -rf $DIR5
    mkdir $DIR5
    echo "Temporary work directory $DIR5 created"
 fi
echo 'Now preparing to calculate VS Enrichment with parameters' 
echo $a 'as actives input and'
echo $b 'as number of inactives/decoys'

for x in `cat dock.list`
 do
	cd $x
	#List the file, get the last line, but suppress the error message. 
	#Usually HTVS, SP has '*lib.maegz' whereas XP has '*_pv.maegz' output (If all stages are run in the same job)
	y=`ls 2>/dev/null *_pv.maegz *lib.maegz | tail -1`
	
	echo 'Calculating Enrichment for job' $x 'with docking output' $y
	
	#Make sure to copy the enrichment.py script to the $ROOT_DIR/$DIR0 directory 
	echo "$SCHRODINGER/run $ROOT_DIR/$DIR0/enrichment-2.2-rOut.py -a $ROOT_DIR/$DIR0/$a -n $b -o ../$DIR2/en_o_$x.csv -p ../$DIR2/en_$x.png $y -r ../$DIR2/en_r_$x.csv > ../$DIR2/en_$x.report"
	      $SCHRODINGER/run $ROOT_DIR/$DIR0/enrichment-2.2-rOut.py -a $ROOT_DIR/$DIR0/$a -n $b -o ../$DIR2/en_o_$x.csv -p ../$DIR2/en_$x.png $y -r ../$DIR2/en_r_$x.csv > ../$DIR2/en_$x.report
	tail -1 ../$DIR2/en_o_$x.csv >> ../$DIR5/en_all_met_value.csv #get only the values
	head -1 ../$DIR2/en_o_$x.csv >> ../$DIR5/en_all_met_title.csv #get only the title
	#Now copy each of the ensemble docked output file to a singe directory named with variable $DIR3
	cp $y ../$DIR3
	echo 'Enrichment calculation for job' $x 'completed'
	cd ..
 done

#Merge the title and enrichment metrices value to a single file
echo `head -1 $ROOT_DIR/$DIR5/en_all_met_title.csv` `cat $ROOT_DIR/$DIR5/en_all_met_value.csv` > $ROOT_DIR/$DIR2/VS_Ensemble_Enrichment_Metrices.csv

echo 'Enrichment result output for all the ensemble is saved as :' 
echo $ROOT_DIR/$DIR2/VS_Ensemble_Enrichment_Metrices.csv
echo "VS Enrichment calculation finished"
#################################################################################################
}
#################################################################################################
#################################################################################################
function vs_rmsd {

echo "Checking for the result data output directory $DIR4 in:"
pwd
if [[ ! -d "$DIR4" ]];
then
    mkdir $DIR4
    echo "RMDS calculation result data output directory $DIR4 created"
else
    echo "RMDS calculation result data output directory $DIR4 already exists."
    echo "Deleting $DIR4"
    rm -rf $DIR4
    mkdir $DIR4
fi

if [[ ! -d "$DIR5" ]];
then
    mkdir $DIR5
    echo "Temporary work directory $DIR5 created"
else
    echo "Temporary work directory $DIR5 already exists."
    echo "Deleting $DIR5"
    rm -rf $DIR5
    mkdir $DIR5
    echo "Temporary work directory $DIR5 created"
fi


cd $ROOT_DIR/$DIR5/

#First, create a name list of docked pose output for each ensemble. 
ls $ROOT_DIR/$DIR3/ | sed 's/.maegz//g' > poses.list


#Read each of the job name from the list and loop over. The variable x is the pose file name without '.maegz'.
for x in `cat poses.list` 
 do
	echo 'Calculating RMSD for pose file' $x.maegz
	$SCHRODINGER/run $ROOT_DIR/$DIR0/rmsd.py -b $ROOT_DIR/$DIR0/$RMSD_REF_POSE_FILE ../$DIR3/$x.maegz -o $x-rmsd.mae > $x-rmsd.log
	echo $x | sed -e 's/'$J1'//g' -e 's/'$J2'//g' -e 's/'$J3'//g' -e 's/OUT_//g' -e 's/_pv//g' > rmsd-$x-1-title.out	
	cat $x-rmsd.log | grep 's_m_title' | awk -F'[ ]' '{ print $6}' >> rmsd-$x-1-title.out
	echo $x | sed -e 's/'$J1'//g' -e 's/'$J2'//g' -e 's/'$J3'//g' -e 's/OUT_//g' -e 's/_pv//g' > rmsd-$x-1-value.out	
	cat $x-rmsd.log | grep 'maxd' | awk -F'[ ]' '{ print $4}' | sed 's/;//g' >> rmsd-$x-1-value.out	
	paste -d',' rmsd-$x-1-title.out rmsd-$x-1-value.out > $ROOT_DIR/$DIR4/RMSD-$x-Table-out.csv	
	echo 'Job for' $x 'completed'
 done

echo "RMSD data extraction completed"
echo "Now working to join the output files"

cd  $ROOT_DIR/$DIR4/
ls  *-out.csv > RMSD-Table-file-names.list
paste -d',' `cat RMSD-Table-file-names.list` > RMSD-Table.tbl

echo "File joining completed. Final file is saved as $ROOT_DIR/RMSD-Table.tbl"
}
#################################################################################################

echo '#######################################################################################################'
echo '# This is Glide VSW Ensemble Data Analysis Script v1.0 | 2011-02-17 |  insilicoscientist@gmail.com    #'
echo '#######################################################################################################'

echo "Current working directory:"
pwd
echo "ROOT_DIR"
echo $ROOT_DIR
echo "Please enter your choice as"
echo "a: for Docking Energy Extraction"
echo "b: for Enrichment metrices calculation"
echo "c: for RMSD calculation or"
echo "q: to Quit the script right now"
echo "Example input: 'ab' for Docking Energy Extraction and Enrichment metrices calculation"
echo "Example input: 'c' for RMSD calculation only"
echo "Choices available: a, ab, ac, b, bc, c, abc, q "
while read i 
do
 if [[ $i == a ]]; then
	echo vs_dee
	vs_dee
	echo
	break;
 elif [[ $i == ab ]]; then
 	echo 'vs_dee vs_en'
	vs_dee
	vs_en
	break;
 elif [[ $i == ac ]]; then
 	echo 'vs_dee vs_rmsd'
	vs_dee
	vs_rmsd
	break;
 elif [[ $i == b ]]; then
 	echo vs_en
	vs_en
	break;
 elif [[ $i == bc ]]; then
 	echo 'vs_en vs_rmsd'
	vs_en
	vs_rmsd
	break;
 elif [[ $i == c ]]; then
 	echo 'vs_rmsd'
	vs_rmsd
	break;
 elif [[ $i == abc ]]; then
 	echo 'vs_dee vs_en vs_rmsd'
	vs_dee
	vs_en
	vs_rmsd
	break;
 elif [[ $i == q ]]; then
 	echo
	echo Bye
	exit;
 else
	echo
	echo "Wrong input"
	exit;
 fi
done

echo '#######################################################################################'
echo '    All jobs finished. Check for errors. If successful, data can be accessed from      '
echo '   '$ROOT_DIR/$DIR1
echo '   '$ROOT_DIR/$DIR2
echo '   '$ROOT_DIR/$DIR3 'and '
echo '   '$ROOT_DIR/$DIR4
echo '    along with '
echo '   '$ROOT_DIR/'Merged_EnsembleVS_Energies.csv'
echo '    ~~~~ Program terminated. Good Bye ~~~~~'
echo '#######################################################################################'