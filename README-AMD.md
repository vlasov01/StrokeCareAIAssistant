1. Setup Conda
conda activate ryzenai-transformers
2. Setup environment variables
cd C:\Users\serge\dev\LocalAIVoiceChat\
setup-amd.ps1
3.
cd C:\AMD\RyzenAI-SW\example\transformers
pip install ops\cpp --force-reinstall
cd C:\AMD\RyzenAI-SW\example\transformers\models\llama2
python run_awq.py --task decode --target aie --w_bit 4
3. Change context with information related to a person by editing chat_params.json file
4. run app
python ai_voicetalk_local.py
5. analyze data by running (it will open a browser window at http://localhost:8501 or http://localhost:8502)
streamlit run show-activity.py
