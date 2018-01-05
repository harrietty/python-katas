'''
The input string represents one of the following:

6-digit hexadecimal - "#RRGGBB"
e.g. "#012345", "#789abc", "#FFA077"
Each pair of digits represents a value of the channel in hexadecimal: 00 to FF
3-digit hexadecimal - "#RGB"
e.g. "#012", "#aaa", "#F5A"
Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.
Preset color name
e.g. "red", "BLUE", "LimeGreen"
You have to use the predefined map PRESET_COLORS (JavaScript, Python, Ruby), presetColors (Java, C#, Haskell), or preset-colors (Clojure). The keys are the names of preset colors in lower-case and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").
'''
PRESET_COLORS = {'gainsboro': '#dcdcdc', 'lightyellow': '#ffffe0', 'mediumseagreen': '#3cb371', 'sandybrown': '#f4a460', 'black': '#000000', 'lime': '#00ff00', 'slategrey': '#708090', 'mediumspringgreen': '#00fa9a', 'springgreen': '#00ff7f', 'darkkhaki': '#bdb76b', 'tan': '#d2b48c', 'darkturquoise': '#00ced1', 'darkviolet': '#9400d3', 'crimson': '#dc143c', 'rebeccapurple': '#663399', 'darkorchid': '#9932cc', 'dodgerblue': '#1e90ff', 'azure': '#f0ffff', 'salmon': '#fa8072', 'aliceblue': '#f0f8ff', 'red': '#ff0000', 'lightgray': '#d3d3d3', 'greenyellow': '#adff2f', 'darkblue': '#00008b', 'navajowhite': '#ffdead', 'saddlebrown': '#8b4513', 'darksalmon': '#e9967a', 'darkolivegreen': '#556b2f', 'orangered': '#ff4500', 'mintcream': '#f5fffa', 'mediumorchid': '#ba55d3', 'lightslategray': '#778899', 'fuchsia': '#ff00ff', 'lightgreen': '#90ee90', 'darkgrey': '#a9a9a9', 'papayawhip': '#ffefd5', 'steelblue': '#4682b4', 'turquoise': '#40e0d0', 'lightcoral': '#f08080', 'yellow': '#ffff00', 'blanchedalmond': '#ffebcd', 'dimgray': '#696969', 'royalblue': '#4169e1', 'palevioletred': '#db7093', 'forestgreen': '#228b22', 'darkred': '#8b0000', 'lavenderblush': '#fff0f5', 'orchid': '#da70d6', 'olive': '#808000', 'cornsilk': '#fff8dc', 'limegreen': '#32cd32', 'blueviolet': '#8a2be2', 'white': '#ffffff', 'lightblue': '#add8e6', 'tomato': '#ff6347', 'bisque': '#ffe4c4', 'mediumpurple': '#9370db', 'magenta': '#ff00ff', 'antiquewhite': '#faebd7', 'hotpink': '#ff69b4', 'whitesmoke': '#f5f5f5', 'darkgoldenrod': '#b8860b', 'coral': '#ff7f50', 'lightpink': '#ffb6c1', 'maroon': '#800000', 'khaki': '#f0e68c', 'moccasin': '#ffe4b5', 'honeydew': '#f0fff0', 'powderblue': '#b0e0e6', 'midnightblue': '#191970', 'palegreen': '#98fb98', 'darkseagreen': '#8fbc8f', 'palegoldenrod': '#eee8aa', 'firebrick': '#b22222', 'aqua': '#00ffff', 'snow': '#fffafa', 'lavender': '#e6e6fa', 'mediumturquoise': '#48d1cc', 'cornflowerblue': '#6495ed', 'seagreen': '#2e8b57', 'darkslategrey': '#2f4f4f', 'mediumaquamarine': '#66cdaa', 'darkslategray': '#2f4f4f', 'slategray': '#708090', 'lightcyan': '#e0ffff', 'lemonchiffon': '#fffacd', 'wheat': '#f5deb3', 'dimgrey': '#696969', 'blue': '#0000ff', 'darkgreen': '#006400', 'skyblue': '#87ceeb', 'darkmagenta': '#8b008b', 'lightgrey': '#d3d3d3', 'lightseagreen': '#20b2aa', 'oldlace': '#fdf5e6', 'floralwhite': '#fffaf0', 'slateblue': '#6a5acd', 'lightsteelblue': '#b0c4de', 'ivory': '#fffff0', 'plum': '#dda0dd', 'indigo': '#4b0082', 'cyan': '#00ffff', 'lightslategrey': '#778899', 'mediumvioletred': '#c71585', 'teal': '#008080', 'burlywood': '#deb887', 'olivedrab': '#6b8e23', 'deepskyblue': '#00bfff', 'yellowgreen': '#9acd32', 'darkorange': '#ff8c00', 'green': '#008000', 'lightskyblue': '#87cefa', 'mistyrose': '#ffe4e1', 'silver': '#c0c0c0', 'navy': '#000080', 'lightsalmon': '#ffa07a', 'rosybrown': '#bc8f8f', 'linen': '#faf0e6', 'sienna': '#a0522d', 'thistle': '#d8bfd8', 'darkgray': '#a9a9a9', 'deeppink': '#ff1493', 'darkcyan': '#008b8b', 'gray': '#808080', 'grey': '#808080', 'indianred': '#cd5c5c', 'cadetblue': '#5f9ea0', 'violet': '#ee82ee', 'chocolate': '#d2691e', 'brown': '#a52a2a', 'mediumslateblue': '#7b68ee', 'beige': '#f5f5dc', 'goldenrod': '#daa520', 'ghostwhite': '#f8f8ff', 'lawngreen': '#7cfc00', 'gold': '#ffd700', 'lightgoldenrodyellow': '#fafad2', 'aquamarine': '#7fffd4', 'peru': '#cd853f', 'darkslateblue': '#483d8b', 'orange': '#ffa500', 'seashell': '#fff5ee', 'mediumblue': '#0000cd', 'pink': '#ffc0cb', 'chartreuse': '#7fff00', 'peachpuff': '#ffdab9', 'purple': '#800080', 'paleturquoise': '#afeeee'}

import re

def parser(strng):
  if strng.lower() in PRESET_COLORS:
    strng = PRESET_COLORS[strng.lower()]
  
  # slice off first #
  strng = strng[1:]

  if len(strng) < 6:
    strng = ''.join([ch * 2 for ch in list(strng)])

  # get groups of 2 
  strng = re.findall(r'.{2}', strng)

  # map each hex pair to int(str, base)
  rgb = [int(pair, 16) for pair in strng]
  return {
    'r': rgb[0],
    'g': rgb[1],
    'b': rgb[2]
  }