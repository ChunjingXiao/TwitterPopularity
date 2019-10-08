
del computePerTweetSensitivity

:: make_feature_buffer.exe is from SVDFeature-master.zip https://github.com/Gnnng/SVDFeature
make_feature_buffer pairwiseRankDataTrain buffer.base.svdpp
make_feature_buffer pairwiseRankDataTest buffer.test.svdpp

:: svd_feature.exe is from PSC\Full  https://sites.google.com/site/kaisongsong/
:: training for 40 rounds
svd_feature pairwiseRank.conf num_round=40

echo off
rename 0040.model temp.save
del *.model
rename temp.save 0040.model
echo on

:: svd_feature_infer.exe is from PSC\Full  https://sites.google.com/site/kaisongsong/
:: write out prediction from 0040.model
svd_feature_infer pairwiseRank.conf pred=40



python computePerTweetSensitivity.py pairwiseRankDataTest pred.txt SelectUserOne computePerTweetSensitivity

python computePerTweetSum.py computePerTweetSensitivity computePerTweetSum.txt


pause
