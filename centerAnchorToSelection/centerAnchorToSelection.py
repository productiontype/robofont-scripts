"""
centerAnchorToSelection
v1.000

Center selected anchor to the x middle position for the selected contour.
Glyph selection only takes into account onCurve points.

"""

from math import sin, radians

g = CurrentGlyph()
font = CurrentFont()



def gatherSelectedOnCurvePoints(glyph):
    li = []
    for p in g.selectedPoints:
        li.append((p.x, p.y))
    return li

def getMinX(glyph):
    return min(gatherSelectedOnCurvePoints(glyph), key = lambda x: x[0] )

def getMaxX(glyph):
    return max(gatherSelectedOnCurvePoints(glyph), key = lambda x: x[0] )

def getMinY(glyph):
    return min(gatherSelectedOnCurvePoints(glyph), key = lambda x: x[1] )

def getMaxY(glyph):
    return max(gatherSelectedOnCurvePoints(glyph), key = lambda x: x[1] )

def getCenterX(glyph):
    return (getMinX(glyph)[0] + getMaxX(glyph)[0])/2

def getCenterY(glyph):
    return (getMinY(glyph)[1] + getMaxY(glyph)[1])/2


def getAnchor(glyph):
    selectedAnchor = []
    for a in glyph.anchors:
        if a.selected == True:
            selectedAnchor.append(a)
    if len(selectedAnchor) != 1:
        print("Please, select only 1 anchor")
        return
        
    else:
        return selectedAnchor[0]


g.prepareUndo()

if font.info.italicAngle is not None:
    anchor = getAnchor(g)

    anchorGlyphDiff = anchor.y - getCenterY(g)
    italicAngle = font.info.italicAngle
    italicAngleMinus = -italicAngle
    angle = 180 - (90 + italicAngleMinus)
    anchorOffset = (anchorGlyphDiff * sin(radians(italicAngleMinus))) / sin(radians(angle))
    anchor.x = round(getCenterX(g) + anchorOffset)

else:
    anchor.x = round(getCenterX(g))

g.changed()
g.performUndo()





