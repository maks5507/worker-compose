# Worker Compose 

**Worker-Compose** is a package for launching and controlling the workers in the microservices architecture or text processing tools.   

**Author:** Maksim Eremeev (me@maksimeremeev.com)

## `Launcher` class

All processing is done via the `Launcher` class.

```python
from worker_compose import Launcher

log_file = 'launcher.log'

launcher = Launcher(log_file=log_file)
```

## Executing the processes

Method `Launcher.launch` executes the processors and workers specified in the `config` file. 

Sample `config.json` has the following form:

```json
{
  "process-id-1": {
    "prefix": "FULL-PATH-TO-PY-SCRIPT",
    "name": "worker",
    
    "init_args": {
      "init_arg_1": "init_arg_value_1",
      "init_arg_2": "init_arg_value_2",
		},
    
    "run_args": {
      "rmq_connect": "amqp://LOGIN:PASSWORD@HOST:PORT",
      "rmq_queue": "WORKER-QUEUE"
    },
    
    "n_jobs": 1,
    "add_process_num": false,
    
    "depends_on": [], 
    "mode": "worker"
  },

  "process-id-2": {
    "prefix": "FULL-PATH-TO-PY-SCRIPT",
    "name": "processor",
    
    "mask": "FILES-MASK",
    "texts": "PATH-TO-TEXT-FOLDER",

    "init_args": {
      "init_arg_1": "init_arg_value_1",
      "init_arg_2": "init_arg_value_2",
    },

    "run_args": {
    },

    "n_jobs": 1,
    "add_process_num": false,

    "depends_on": [],
    "mode": "processor"
  }
}

```

 The process pool is then executed by `launcher.launch('config.json')`.