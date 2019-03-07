

for /L %%i in (13,1,13) do (
		echo %%i
		
		python train.py %%i

		python eval.py --eval_train --checkpoint_dir="./runs/1500000000/checkpoints/"


		python ComputeSenSpeGM.py runs\1500000000\prediction.csv data\RandomTestTxt.pos data\RandomTestTxt.neg zPred%%i.txt
		
)


pause
