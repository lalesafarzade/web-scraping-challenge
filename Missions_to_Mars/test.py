# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# List of dictionaries
listings = {'news_title': 'Mars Scientists Investigate Ancient Life in Australia', 'news_p': "Teams with NASA's Mars 2020 and ESA's ExoMars practiced hunting for fossilized microbial life in the Australian Outback in preparation for their Red Planet missions. ", 'news_date': 'March 10, 2022', 'news_img':'https://mars.nasa.gov/system/news_items/list_view_images/8520_PIA23466-226.jpg', 'feuture_img_url': 'https://spaceimages-mars.com/image/featured/mars2.jpg', 'tables': '<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Mars</th>  <th>Earth</th>    </tr>    <tr>      <th>Mars - Earth Comparison</th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Diameter:</th>      <td>6,779 km</td>      <td>12,742 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.39 × 10^23 kg</td>      <td>5.97 × 10^24 kg</td>    </tr>    <tr>      <th>Moons:</th>      <td>2</td>      <td>1</td>    </tr>    <tr>      <th>Distance from Sun:</th>      <td>227,943,824 km</td>      <td>149,598,262 km</td> </tr>    <tr>      <th>Length of Year:</th>      <td>687 Earth days</td>      <td>365.24 days</td>    </tr>    <tr>      <th>Temperature:</th>      <td>-87 to -5 °C</td>      <td>-88 to 58°C</td>    </tr>  </tbody></table>', 'hemisphere_image_urls': [{'img_url': 'https://marshemispheres.com/images/full.jpg', 'title': 'Cerberus Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg', 'title': 'Schiaparelli Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg', 'title': 'Syrtis Major Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg', 'title': 'Valles Marineris Hemisphere Enhanced'}]}

# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html", listings=listings)


if __name__ == "__main__":
    app.run(debug=True)


