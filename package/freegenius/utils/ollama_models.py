ollama_models = (
    "falcon2",
    "falcon2:11b",
    "llama3-chatqa",
    "llama3-chatqa:8b",
    "llama3-chatqa:70b",
    "llava-phi3",
    "llava-phi3:3.8b",
    "llava-llama3",
    "llava-llama3:8b",
    "llama3-gradient",
    "llama3-gradient:8b",
    "llama3-gradient:70b",
    "moondream",
    "moondream:1.8b",
    "dolphin-llama3",
    "dolphin-llama3:8b",
    "llama3",
    "llama3:8b",
    "llama3:8b-text",
    "llama3:70b-instruct",
    "llama3:70b-text",
    "wizardlm2",
    "wizardlm2:7b",
    "wizardlm2:8x22b",
    #"wizardlm2:70b", # coming soon
    "codeqwen",
    "codeqwen:7b-chat",
    "codeqwen:7b-code",
    "dbrx",
    "dbrx:132b",
    "command-r-plus",
    "command-r-plus:104b",
    "gemma",
    "gemma:2b",
    "gemma:7b",
    "llama2",
    "llama2:7b",
    "llama2:13b",
    "llama2:70b",
    "mistral",
    "mistral:7b",
    "mixtral",
    "mixtral:8x7b",
    "mixtral:instruct",
    "mixtral:text",
    "mixtral:8x22b",
    "mixtral:8x22b-instruct",
    "mixtral:8x22b-text",
    "neural-chat",
    "dolphin-mixtral",
    "dolphin-mixtral:8x7b",
    "mistral-openorca",
    "mistral-openorca:7b",
    "llama2-uncensored",
    "llama2-uncensored:7b",
    "llama2-uncensored:70b",
    "orca-mini",
    "orca-mini:3b",
    "orca-mini:7b",
    "orca-mini:13b",
    "orca-mini:70b",
    "phi3",
    "phi3:3.8b",
    "phi",
    "phi:2.7b",
    "dolphin-mistral",
    "dolphin-mistral:7b",
    "vicuna",
    "vicuna:7b",
    "vicuna:13b",
    "vicuna:33b",
    "wizard-vicuna-uncensored",
    "wizard-vicuna-uncensored:7b",
    "wizard-vicuna-uncensored:13b",
    "wizard-vicuna-uncensored:30b",
    "zephyr",
    "openhermes",
    "llama2-chinese",
    "llama2-chinese:7b",
    "llama2-chinese:13b",
    "tinyllama",
    "openchat",
    "qwen",
    "qwen:0.5b",
    "qwen:1.8b",
    "qwen:4b",
    "qwen:7b",
    "qwen:14b",
    "qwen:72b",
    "orca2",
    "orca2:7b",
    "orca2:13b",
    "falcon",
    "falcon:7b",
    "falcon:40b",
    "falcon:180b",
    "nous-hermes",
    "nous-hermes:7b",
    "nous-hermes:13b",
    "nous-hermes:70b",
    "dolphin-phi",
    "starling-lm",
    "starling-lm:7b",
    "medllama2",
    "yi",
    "yi:6b",
    "yi:34b",
    "wizardlm-uncensored",
    "everythinglm",
    "stable-beluga",
    "stable-beluga:7b",
    "stable-beluga:13b",
    "stable-beluga:70b",
    "solar",
    "tinydolphin",
    "yarn-mistral",
    "nous-hermes2-mixtral",
    "nous-hermes2-mixtral:dpo",
    "nous-hermes2-mixtral:8x7b",
    "samantha-mistral",
    "stablelm-zephyr",
    "wizard-vicuna",
    "meditron",
    "meditron:7b",
    "meditron:70b",
    "yarn-llama2",
    "yarn-llama2:7b",
    "yarn-llama2:13b",
    "stablelm2",
    "nous-hermes2",
    "nous-hermes2:10.7b",
    "nous-hermes2:34b",
    "deepseek-llm",
    "deepseek-llm:7b",
    "deepseek-llm:67b",
    "open-orca-platypus2",
    "llama-pro",
    "nexusraven",
    "mistrallite",
    "goliath",
    "notux",
    "alfred",
    "megadolphin",
    "wizardlm",
    "wizardlm:7b",
    "wizardlm:13b",
    "wizardlm:30b",
    "wizardlm:70b",
    "xwinlm",
    "xwinlm:7b",
    "xwinlm:13b",
    "xwinlm:70b",
    "notus",
    "command-r",
    # vision models
    "llava",
    "llava:7b",
    "llava:13b",
    "llava:34b",
    "bakllava",
    "bakllava:7b",
    # embeddings
    "snowflake-arctic-embed",
    "snowflake-arctic-embed:22m",
    "snowflake-arctic-embed:33m",
    "snowflake-arctic-embed:110m",
    "snowflake-arctic-embed:137m",
    "snowflake-arctic-embed:335m",
    "nomic-embed-text",
    "all-minilm",
    "mxbai-embed-large",
    # code models
    "magicoder",
    "magicoder:7b",
    "codebooga",
    "codebooga:34b",
    "wizardcoder",
    "wizardcoder:33b",
    "wizardcoder:python",
    "wizardcoder:7b-python",
    "wizardcoder:13b-python",
    "wizardcoder:34b-python",
    "phind-codellama",
    "phind-codellama:34b",
    "phind-codellama:34b-python",
    "codegemma",
    "codegemma:7b-instruct",
    "codegemma:7b-code",
    "codegemma:2b-code",
    "codellama",
    "codellama:7b-instruct",
    "codellama:13b-instruct",
    "codellama:34b-instruct",
    "codellama:70b-instruct",
    "codellama:7b-python",
    "codellama:13b-python",
    "codellama:34b-python",
    "codellama:70b-python",
    "codellama:7b-code",
    "codellama:13b-code",
    "codellama:34b-code",
    "codellama:70b-code",
    "stable-code",
    "stable-code:3b-code",
    "stable-code:3b-instruct",
    "codeup",
    "codeup:13b",
    "codeup:13b-llama2",
    "codeup:13b-llama2-chat",
    "deepseek-coder",
    "deepseek-coder:1.3b-instruct",
    "deepseek-coder:6.7b-instruct",
    "deepseek-coder:33b-instruct",
    "deepseek-coder:1.3b-base",
    "deepseek-coder:6.7b-base",
    "deepseek-coder:33b-base",
    "starcoder",
    "starcoder:1b",
    "starcoder:3b",
    "starcoder:7b",
    "starcoder:15b",
    "starcoder2",
    "starcoder2:3b",
    "starcoder2:7b",
    "starcoder2:15b",
    "dolphincoder",
    "dolphincoder:7b",
    "dolphincoder:15b",
    # sql
    "duckdb-nsql",
    "duckdb-nsql:7b",
    "sqlcoder",
    "sqlcoder:7b",
    "sqlcoder:15b",
    "sqlcoder:70b",
    # math
    "wizard-math",
    "wizard-math:7b",
    "wizard-math:13b",
    "wizard-math:70b",
)