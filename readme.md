# Reinforcement Learning in Action

- Like most environments that involve a negative and a positive reward, we devise our environment in a similar manner. With multiple tasks focusing on various skillset for the agent to adapt for and learn, the goal is set to not just maximize reward but also ensure there is a balance between exploitation and exploration. 

The purpose was to allow the agent to nomad around, and get mechanically strive to live; to draw parallel with human instincts. We then introduce Proximal Policy Optimization in the agent’s learning gradient, therefore discussing how drastic the changes are. 

<img width="500" alt="image" src="https://github.com/SteveMama/FAI-VIZDOOM/assets/17807913/7481e785-a224-420e-9867-b829a8acc038">


- The github repo is official implementation of the submitted project report titled **"Reinforcement Learning in Action"**
- This repo draws its inspiration from Huggingface's Reinforcement Learning Course.
- We adopt the workflow and dynamic structure of Sample Factory for the ease of implementation, however, significant changes have been made to accommodate custom architecture, multiple workers and visual result logging.
- For demo purposes, we've included a few output videos that are recorded sessions of the agent's learning at various episodes checkpoints.

## Usage

**NOTE: Each task takes more than 3 hours to train and provide a resulting output. We ran our experiments on a GTX2050 GPU due to restrictions on google colab runtimes. Implementing the same on Discovery Cluster should also be sufficient.**

- Import the jupyter Python notebook in your local or hosted environment.
- Ensure all the needed libraries are installed.

```
!apt-get install build-essential zlib1g-dev libsdl2-dev libjpeg-dev \
nasm tar libbz2-dev libgtk2.0-dev cmake git libfluidsynth-dev libgme-dev \
libopenal-dev timidity libwildmidi-dev unzip ffmpeg

apt-get install libboost-all-dev

apt-get install liblua5.1-dev
```

- Clone the FAI-VIZDOOM repository and install all the necessary dependencies.

``` 
!pip install faster-fifo==1.4.2
!pip install vizdoom

!git clone https://github.com/SteveMama/FAI-VIZDOOM.git 
%cd FAI-VIZDOOM/
!pip install -e .
```

- with this you, can run the remaning cells that should give you a similar output as the videos attached speak.

- you can decrease the  ``` --num_episodes``` command incase your environment isn't able handle 100000 episodes at the first instance.
- You should start noticing considerable performance change after 30,000 episodes.


### Team Memebers
- Pranav K
- Sai Chandu
- Parijat C
- Smit Dar
