# 11.2 Folds - structural geology

**Outline:**
* Folds
* Measuring strike and dip of a plane
* Stereonets


## Additional Assigned Reading

Physical Geology – 2nd Edition, By Steven Earle [Chapter 12 Geologic Structures](https://opentextbc.ca/physicalgeology2ed/part/chapter-12-geological-structures/) focusing in particular on [Chapter 12.2 Folding](https://opentextbc.ca/physicalgeology2ed/chapter/12-2-folding/) and [Chapter 12.4 Measuring Geological Structures](https://opentextbc.ca/physicalgeology2ed/chapter/12-4-measuring-geological-structures/).


## Geologic Model Activity

Go to [Visible Geology](https://app.visiblegeology.com/) and play around with it! Start by clicking "Visualize" then follow the prompts to add geologic beds, folds, tilts, topography. Reset and start-over a few times to build some structural geology intuition. 

![](./images/visual_geo_example.png)



## Folds

When rocks are squeezed by tectonic stresses they will either bend or break depending on their material properties (e.g. composition) and temperature and pressure conditions. We have already learned about brittle ruptures i.e. earthquakes. Now let's cover folding.

Folding terminalogy:
* Folding axis - the plane that cuts through the crest of the fold
* Folding limbs - the tilted beds on either side of the folding axial plane
* Syncline or synform - a upward fold
* Anticline or antiform - an downward fold

![](./images/folding_jargon.png)
> A cartoon cross section of folded beds.

Studying the direction and extent of folding help structural geologists estimate the regional tectonic stresses.

## Measuring strike and dip

Strike and dip are two measurements used to describe the orientation of a plane, such as the limb of a fold. Strike is measured from a horizontal line that lies in the plane, it is the direction in degrees from north (like azimuth which we covered) of the horizontal line. Strike is measured with a compass. Dip is the angle from horizontal that the plane is tilted, and it is measured with an clinometer. Strike and dip are plotted on maps as a "T" shape that points along strike and down slope.

![](./images/strike_dip_cartoon.png)
> A cartoon cross section of folded beds, which also shows the surface and a strike and dip of one of the fold limbs.


Watch this video about measureing strike and dip:

[![](http://img.youtube.com/vi/FbXhooadhZw/0.jpg)](http://www.youtube.com/watch?v=FbXhooadhZw "")


## Plotting planes and lines on a stereonet

Stereonets are a 2D graphical representation of the orientiation of lines and planes in 3D. On a stereonet a plane will appear as a line, and a line as a point. The strike is depicted as the angle clockwise from north that the line meets the edge of the plot. The dip is depicted as the distance of the line from the edge. Lines close the edge are close to horizontal and lines near the center are nearly vertical. The way to visualize this is a stereonet is the 2D projection of looking down at the plane in a hemsphere:

![](./images/stereonet_bowl.png)

The "pole to a plane" is a line the is perpandicular to the plane. So it will plot 90 degrees away.

import matplotlib.pyplot as plt
import mplstereonet

fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

strike, dip = 110, 30
ax.plane(strike, dip, 'g-', linewidth=2)
ax.pole(strike, dip, 'g^', markersize=10)
ax.grid()
ax.legend(['Plane','Pole'])
plt.show()