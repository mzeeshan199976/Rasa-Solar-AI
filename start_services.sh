if [ -z "$PORT"]
then
  PORT=8080
fi
rasa run --model models --enable-api --cors "*" --debug --port $PORT