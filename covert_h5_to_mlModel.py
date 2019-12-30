
import coremltools

# output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# your_model = coremltools.converters.keras.convert('final_model.h5', input_names=['image'], output_names=['output'], class_labels=output_labels, image_input_names='image')
# coreml_model = coremltools.converters.keras.convert('final_model.h5', input_names = 'image', image_input_names = 'image', class_labels = ['cat', 'dog'], output_names = 'output')
# coreml_model.save('MyModel.mlmodel')
# print("welcome")


coreml_model = coremltools.converters.keras.convert('model.h5', input_names=['image'], output_names=['output'],image_input_names='image')

coreml_model.author = 'Jimoh Babatunde'
coreml_model.short_description = 'Cat Dog Classifier converted from a Keras model'
coreml_model.input_description['image'] = 'Takes as input an image'
coreml_model.output_description['output'] = 'Prediction as cat or dog'
coreml_model.save('MyModel.mlmodel')
