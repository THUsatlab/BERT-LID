python run_me.py --num_train_epochs=150.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=175.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=200.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=225.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=250.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=275.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=300.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=325.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=350.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=375.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=400.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=1 --print_step=10
python run_me.py --num_train_epochs=150.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=175.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=200.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=225.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=250.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=275.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=300.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=325.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=350.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=375.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=400.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=2 --print_step=10
python run_me.py --num_train_epochs=150.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=175.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=200.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=225.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=250.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=275.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=300.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=325.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=350.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=375.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10
python run_me.py --num_train_epochs=400.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=4 --print_step=10

python run_me.py --max_seq_length=65 --num_train_epochs=5.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=8 --print_step=100 > BertOrigin.out 2>&1 &
python run_me.py --max_seq_length=65 --num_train_epochs=5.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=8 --print_step=100 > BertCNN.out 2>&1 &
python run_me.py --max_seq_length=65 --num_train_epochs=5.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=8 --print_step=100 > BertATT.out 2>&1 &
python run_me.py --max_seq_length=65 --num_train_epochs=5.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=8 --print_step=100 > BertRCNN.out 2>&1 &
python run_me.py --max_seq_length=65 --num_train_epochs=5.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=8 --print_step=100 > BertCNNPlus.out 2>&1 &
python run_me.py --max_seq_length=65 --num_train_epochs=5.0 --do_train --gpu_ids="7" --gradient_accumulation_steps=8 --print_step=100 > BertDPCNN.out 2>&1 &