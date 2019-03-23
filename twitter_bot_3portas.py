import tweepy
import time
import random

print('this is my twitter bot')

CONSUMER_KEY      = '****'
CONSUMER_SECRET   = '****'
ACCESS_KEY        = '****'
ACCESS_SECRET     = '****'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file_name = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def select_image():
    numero = random.randint(1,11)
    return numero


def reply_to_tweets():
    print('recebendo e respondendo tweets.....')
    last_seen_id = retrieve_last_seen_id(file_name)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, file_name)
        if 'carro' in mention.full_text.lower():
            print('carro encontrado em: ' + mention.full_text + '\n\n')
            #api.update_status('@' + mention.user.screen_name +  ' aqui lhe trago um carro com tres porta kkkkkkk', mention.id)  
            imagem = select_image()
            imagePath = 'carros/' + str(imagem) + '.jpg'
            status = '@' + mention.user.screen_name +  ' aqui lhe trago um carro com tres porta kkkkkkk'
            
            api.update_with_media(imagePath, status, in_reply_to_status_id = mention.id)     

while True:
    reply_to_tweets()
    time.sleep(45)