1. Follow https://github.com/amd/RyzenAI-SW/blob/main/example/transformers/models/llm/docs/README.md
2. Setup environment variables
setup-amd.ps1
3. Change context with information related to a person by editing chat_params.json file
4. Run app
python ai_voicetalk_local.py
5. analyze data by running (it will open a browser window at http://localhost:8501 or http://localhost:8502)
streamlit run show-activity.py
