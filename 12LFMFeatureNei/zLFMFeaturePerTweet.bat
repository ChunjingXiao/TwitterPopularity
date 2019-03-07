
echo off
del computePerTweetSensitivity



set currDir=%cd%
cd..
set lastDir=%cd%
cd %currDir%

set data=%lastDir%/2DataRandom
set tempData=7DataCache


cd %tempData%
del SelectUserOneNum
cd..


for /L %%i in (1,1,1500) do (
		echo %%i
		echo 1 SelectUserOne.py
		python %lastDir%/1LibRandom/SelectUserOne.py %data%/SelectUserProfile %tempData%/SelectUserOneNum %tempData%/SelectUserOne

		echo 2 TweetTimeRtSparseSelect.py
		python %lastDir%/1LibRandom/TweetTimeRtSparseSelect.py %tempData%/SelectUserOne %data%/TweetTimeRtSparseClean %tempData%/TweetTimeRtSparseSelect

		echo 3 pairwiseRankData.py
		python pairwiseRankData.py %tempData%/TweetTimeRtSparseSelect %tempData%/pairwiseRankData

		echo 4 DivideTrainTest.py
		python %lastDir%/1LibRandom/DivideTrainTest.py %tempData%/pairwiseRankData %tempData%/pairwiseRankDataTrain %tempData%/pairwiseRankDataTest

		echo 5 make_feature_buffer
		%lastDir%/1LibRandom/make_feature_buffer %tempData%/pairwiseRankDataTrain %tempData%/buffer.base.svdpp
		%lastDir%/1LibRandom/make_feature_buffer %tempData%/pairwiseRankDataTest %tempData%/buffer.test.svdpp

		echo 6 svd_feature
		%lastDir%/1LibRandom/svd_feature pairwiseRank.conf num_round=80
		%lastDir%/1LibRandom/svd_feature_infer pairwiseRank.conf pred=80

		echo 7 computePerTweetSensitivity.py
		python %lastDir%/1LibRandom/computePerTweetSensitivity.py %tempData%/pairwiseRankDataTest pred.txt %tempData%/SelectUserOne computePerTweetSensitivity

)


python %lastDir%/1LibRandom/computePerTweetSum.py computePerTweetSensitivity computePerTweetSum.txt

del computePerTweetSensitivity


cd %tempData%
rename 0040.model temp.save
del *.model
rename temp.save 0040.model
echo on
cd..
del pred.txt


pause
