import os
from imageai.Classification import ImageClassification

exec_path = os.getcwd()

prediction = ImageClassification()

prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path,'mobilenet_v2-b0353104.pth'))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(exec_path,'godzilla.jpg'), result_count=5)
for prediction, probability in zip(predictions, probabilities):
    print(f'{prediction} : {probability}')


 storeAccount.getAccountById()
    .then((result)=> {
        //logic if success
    }).catch((error) => {
        //logic if error
    }) 

