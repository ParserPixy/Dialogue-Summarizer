import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model= model_pegasus)

        #loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        #reading from yaml file
        trainer_args = TrainingArguments(
            output_dir = self.config.root_dir,
            num_train_epochs = self.config.num_train_epochs,
            per_device_train_batch_size = self.config.per_device_train_batch_size,
            per_device_eval_batch_size= self.config.per_device_train_batch_size,
            save_steps = float(self.config.save_steps),
            eval_strategy = self.config.eval_strategy,
            eval_steps = self.config.eval_steps,
            logging_steps = self.config.logging_steps,
            warmup_steps = self.config.warmup_steps,
            weight_decay = self.config.weight_decay,
            gradient_accumulation_steps = self.config.gradient_accumulation_steps
        )

        # #inputting own args
        # trainer_args = TrainingArguments(
        #     output_dir = self.config.root_dir,
        #     num_train_epochs = 1,
        #     per_device_train_batch_size = 1,
        #     per_device_eval_batch_size = 1,
        #     save_steps = float(1e6),
        #     eval_strategy = 'steps',
        #     eval_steps = 500,
        #     logging_steps = 10,
        #     warmup_steps = 500,
        #     weight_decay = 0.01,
        #     gradient_accumulation_steps = 16
        # )

        trainer = Trainer(model = model_pegasus, args = trainer_args,
                          tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                            train_dataset = dataset_samsum_pt['test'],
                            eval_dataset = dataset_samsum_pt['validation'])
        
        trainer.train()

        ## Save model
        model_pegasus.save_pretrained(os.path.jo
        
        
        in(self.config.root_dir,"pegasus-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-tokenizer"))