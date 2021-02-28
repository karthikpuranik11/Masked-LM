from simpletransformers.t5 import T5Model
from os import cpu_count

model_args = {
    "cache_dir": "next_word_500",
    "output_dir": "next_word_output_500",
#    "best_model_dir":"1M_outputs_new/best_model",
#    "reprocess_input_data": True,
    'fp16': False,
    "fp16_opt_level" : "03",
    "overwrite_output_dir": True,
    "max_seq_length": 64,
    "train_batch_size": 16,
    "num_train_epochs": 10,
    "save_model_every_epoch": True,
    "save_steps": 266000,
#    "thread_count":1,
#    "dataloader_num_workers": 0,
#    "reprocess_input_data": False,
    "process_count": cpu_count() - 2 if cpu_count() > 2 else 1,
    "num_beams": None,
    "do_sample": True,
    "max_length": 50,
    "top_k": 50,
    "top_p": 0.95,
    "use_multiprocessing": False,
    "num_return_sequences": 5,
}

#loading the model
new_model = T5Model("t5","/content/next_word_output_500", args=model_args, cuda_use=True)