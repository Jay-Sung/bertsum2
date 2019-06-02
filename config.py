from bunch import Bunch


config = {
    "SEQ_LEN": 4,
    "MAX_EXAMPLE_LEN": 512,
    "BATCH_SIZE": 2,
    "BUFFER_SIZE": 1,
    "VOCAB_LEN": 30522,
    "LOGDIR": 'log'
}

config = Bunch(config)


