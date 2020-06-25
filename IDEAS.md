<h1> Ideas </h1>

<ul>
    <li>To measure sharpness and curvature, we can develop an equation that models robot wheel speed as a function of radius</li>
    <li>Measure what each wheel speed must be to rotate to a given angle</li>
    <li>My other idea was to calculate the time difference between the time one sensor is False, and when both sensors are False </li>
    <li>Additionally, perhaps we can implement DQL or even an RNN using OpenAI or our own 'simulated' environment</li>
    <ul>
        <li>I don't have any experience with game developing but im sure making a curved line can't be too difficult. And besides we can always just use the robot. However now I'm thinking about it, this idea seems highly impractical. What if it predicted curvature of the next (i dunno) 5 inches of line, and then kept going via a recurrent neural network?</li>
        <li>The inputs would be the time difference between the boolean operators and also which operator was first to go off</li>
        <li>The output would be of size 2, and come out as the left and right wheel speeds</li>
    <ul>
</ul>

<br>
Ideally we want to be able to give the robot a radius, place it on the circle, and then have be able to drive all the way around circle lickety split.
We might be able to do that with Bezier Curves and even De Casteljau's Recursive Algorithm (Splits up big curve into a lot of small arbitrary curves)


Great Sources

We could build differential drive simulations on Gazebo or other robotics simulation software.

http://rossum.sourceforge.net/papers/DiffSteer/DiffSteer.html
https://www.youtube.com/watch?v=pnYccz1Ha34