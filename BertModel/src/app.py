import config
import torch
import flask
from flask import Flask
from flask import request
from model import BERTBaseUncased

app = Flask(__name__)

MODEL= None 
DEVICE=  torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def tweet_prediction(tweet,model):
    tokenizer= config.TOKENIZER
    max_len = config.MAX_LEN
    tweetstr = str(tweet)
    review = " ".join(review.split())

    inputs = tokenizer.encode_plus(
        review,
        None,
        add_special_tokens = True,
        max_length=max_len
    )

        ids = inputs['input_ids']
        mask = inputs['attention_mask']
        token_type_ids= inputs['token_type_ids']

        padding_length =max_len - len(ids)
            
        ids = ids +([0]*padding_length)
        mask = mask +([0]*padding_length)
        token_type_ids = token_type_ids +([0]*padding_length)

        ids= torch.tensor(ids, dtype=torch.long),
        mask= torch.tensor(mask, dtype=torch.long),
        token_type_ids= torch.tensor(token_type_ids, dtype=torch.long),
        
        ids = ids.to(DEVICE, dtype=torch.long).unsqueeze(0)
        token_type_ids = token_type_ids.to(DEVICE, dtype=torch.long).unsqueeze(0)
        mask = mask.to(DEVICE, dtype=torch.long).unsqueeze(0)
       

        output = model(
            ids=ids,
            mask=mask,
            token_type_ids=token_type_ids
        )

        outputs = torch.sigmoid(outputs).cpu().detatch.numpy()
        return outputs[0][0]
@app.route('/predict')

def predict():
    tweet = request.args.get('tweet')
    positive_prediction = tweet_prediction(tweet,model= MODEL)
    negative_prediction= 1- positive_prediction
    print(tweet)
    reponse = {}
    response['response']={
        'postive':str(positive_prediction),
        'negative':str(negative_prediction),
        'sentence':str(sentence)
    }

    return flask.jsonify(response)

if __name__ == '__main__':
    MODEL=BERTBaseUncased()
    MODEL.to(DEVICE)
    MODEL.eval()
    app.run()
