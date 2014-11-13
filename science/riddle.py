from matplotlib import pyplot as plt
import numpy as np
import sys



def walk(steps=1000,walks=200):
    """
    We have a line of points a unit distance from each other
    a walker takes a random step in any direction, 
    we check the distance from the origin after n steps.

            --------------> time steps   (implemented as +1 or -1 in code at each point)
	 |       --o--o--o--o--o--o--o--o--o--o--o--o
	 |       --o--o--o--o--o--o--o--o--o--o--o--o
	 |       --o--o--o--o--o--o--o--o--o--o--o--o
	 |       --o--o--o--o--o--o--o--o--o--o--o--o
	\|/      --o--o--o--o--o--o--o--o--o--o--o--o
	walks    --o--o--o--o--o--o--o--o--o--o--o--o
	         --o--o--o--o--o--o--o--o--o--o--o--o
     
    we do the distance calcuation using 
    """

    walks = 1000  # number of walks
    steps = 200   # time during which we follow the walker
    # We randomly choose all the steps 1 or -1 of the walk
    walk = 2 * ( np.random.random_integers(0, 1, (walks,steps)) - 0.5 )
    np.unique(walk) # Verification : all steps are 1 or -1
    # We build the walks by summing steps along the time
    cumulative_walk = np.cumsum(walk, axis=1) # axis = 1 : dimension of time
    #  walk = [  1 1 -1 1 1...
    #            1 ...
    #           -1 ...
    #  cumulative_walk= [ 1 2 1 2 3 
    #                     1 ...
    #                    -1 ..

    square_distance = cumulative_walk**2
    # We get the mean in the axis of the steps
    mean_sq_distance = np.mean(square_distance, axis=0)
    plt.figure()
    plt.plot(mean_sq_distance)
    plt.figure()
    plt.plot(np.sqrt(mean_sq_distance))
    plt.show()


if __name__ == "__main__":
    steps = int(sys.argv[1])
    walks = int(sys.argv[2])
    walk(steps,walks)

