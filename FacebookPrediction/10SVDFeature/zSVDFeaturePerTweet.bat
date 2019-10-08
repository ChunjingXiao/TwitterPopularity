
echo off
del computePerTweetSensitivity
del computePerUserSensitivity



set currDir=%cd%
cd..
set lastDir=%cd%
cd %currDir%

set tempDat=7DataCache

::for /l %%k in (0,1,9) do (
::for /l %%k in (1,1,1) do (
::    echo %%k

cd 7DataCache
del SelectUserOneNum
cd..


for /L %%i in (1,1,1500) do (
		echo %%i
		echo 1SelectUserOne/SelectUserOne.py
		python %lastDir%/1SelectUserOne/SelectUserOne.py SelectUserProfile %tempDat%/SelectUserOneNum %tempDat%/SelectUserOne

		echo 2TweetTimeRtSparseSelect/TweetTimeRtSparseSelect.py
		python %lastDir%/2TweetTimeRtSparseSelect/TweetTimeRtSparseSelect.py %tempDat%/SelectUserOne TweetTimeRtSparseClean %tempDat%/TweetTimeRtSparseSelect

		echo 3PairwiseRankData/pairwiseRankData.py
		python 3PairwiseRankData/pairwiseRankData.py %tempDat%/TweetTimeRtSparseSelect %tempDat%/pairwiseRankData

		echo 4DivideTrainTest/DivideTrainTest.py
		python %lastDir%/4DivideTrainTest/DivideTrainTest.py %tempDat%/pairwiseRankData %tempDat%/pairwiseRankDataTrain %tempDat%/pairwiseRankDataTest

		echo 5SvdFeaturePredict/make_feature_buffer
		:: make_feature_buffer.exe is from SVDFeature-master.zip https://github.com/Gnnng/SVDFeature
		%lastDir%/5SvdFeaturePredict/make_feature_buffer %tempDat%/pairwiseRankDataTrain %tempDat%/buffer.base.svdpp
		%lastDir%/5SvdFeaturePredict/make_feature_buffer %tempDat%/pairwiseRankDataTest %tempDat%/buffer.test.svdpp

		echo 5SvdFeaturePredict/svd_feature
		:: svd_feature.exe is from PSC\Full  https://sites.google.com/site/kaisongsong/ ;; training for 40 rounds
		%lastDir%/5SvdFeaturePredict/svd_feature pairwiseRank.conf num_round=80
		%lastDir%/5SvdFeaturePredict/svd_feature_infer pairwiseRank.conf pred=80

		echo 5SvdFeaturePredict/computeSensitivityPerTweet.py
		rem python %lastDir%/5SvdFeaturePredict/computeSensitivityPerUser.py %tempDat%/pairwiseRankDataTest pred.txt SelectUserProfile computeSensitivityPerUser
		
		
		python %lastDir%/5SvdFeaturePredict/computePerTweetSensitivity.py %tempDat%/pairwiseRankDataTest pred.txt %tempDat%/SelectUserOne computePerTweetSensitivity

)

::)

python %lastDir%/5SvdFeaturePredict/computePerTweetSum.py computePerTweetSensitivity computePerTweetSum.txt

cd 7DataCache
rename 0040.model temp.save
del *.model
rename temp.save 0040.model
echo on
cd..
del pred.txt

pause
