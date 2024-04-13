@echo off
cd /d "C:\Users\tal22\Documents\Project\my_samannotator"
python annotator.py --app_resolution 1080,1920 --model_type vit_b --keep_input_size True --max_size 720 --quality_control_mode True
