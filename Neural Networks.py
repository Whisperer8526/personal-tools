start = 0.0001
min = 0.00001
max = 0.001
rampup_epochs = 10
sustain_epochs = 10
decay = .8

def lrfn(epoch):
  if epoch < rampup_epochs:
    return (max - start)/rampup_epochs * epoch + start
  elif epoch < rampup_epochs + sustain_epochs:
    return max
  else:
    return min
    
lr = keras.callbacks.LearningRateScheduler(lambda epoch: lrfn(epoch), verbose=True)


def plot_loss(history, min, max):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.ylim([min, max])
  plt.xlabel('Epoch')
  plt.ylabel('Error')
  plt.legend()
  plt.grid(True)
