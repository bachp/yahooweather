import logging
from yahooweather import YahooWeather, get_woeid, UNIT_C

logging.basicConfig(level=logging.DEBUG)

yweather = YahooWeather(91543049, UNIT_C)
if yweather.updateWeather():
    print("RawData: %s" % str(yweather.RawData))
    print("Units: %s" % str(yweather.Units))
    print("Now: %s" % str(yweather.Now))
    print("Forecast: %s" % str(yweather.Forecast))
    print("Wind: %s" % str(yweather.Wind))
    print("Atmosphere: %s" % str(yweather.Atmosphere))
    print("Astronomy: %s" % str(yweather.Astronomy))

    data = yweather.Now
    print("Weather image from current: %s" %
          yweather.getWeatherImage(data["code"]))

    print("The woeid from Gstaad is: %s" % get_woeid(46.475661, 7.283469))

else:
    print("Can't read data from yahoo!")
