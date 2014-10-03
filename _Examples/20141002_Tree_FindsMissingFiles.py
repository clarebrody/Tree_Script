#       Initialize the missingFrames list and counters
        missingFrames = []
        firstMissingFrame = None
        lastMissingFrame = None
        i = 0
#       While we haven't reached the end of our range
        while i < len(frameRange):
#           If the frame supposed to be there is there
            if frameRange[i] in frameList:
#               And we have set the firstMissingFrame
                if firstMissingFrame is not None and lastMissingFrame is None:
#                   We're only missing a single frame in a row, so append it
#                   and reset the counters
                    missingFrames.append(str(firstMissingFrame))
                    firstMissingFrame = None
                    lastMissingFrame = None
#               Or if first and last missing are set
                elif firstMissingFrame is not None and lastMissingFrame is not None:
#                   Then there was more than one in a row, so append a range
#                   and reset the counters
                    missingFrames.append(str(firstMissingFrame)+"-"+str(lastMissingFrame))
                    firstMissingFrame = None
                    lastMissingFrame = None
#               And then move on
                i += 1
#           If the frame supposed to be there is NOT there
            else:
#               And we are on the last frame
                if frameRange[i] == int(endFrame):
#                   If the firstMissingFrame isn't set, set this as the first missing
                    if firstMissingFrame == None:
                        firstMissingFrame = frameRange[i]
#                   But if the first is set, then set this as the last missing
                    else:
                        lastMissingFrame = frameRange[i]
#                   Then, if only the first missing was set
                    if firstMissingFrame is not None and lastMissingFrame is None:
#                       We're only missing a single frame in a row, so append it
                        missingFrames.append(str(firstMissingFrame))
                        firstMissingFrame = None
                        lastMissingFrame = None
#                   Or if the first and last missing was set
                    elif firstMissingFrame is not None and lastMissingFrame is not None:
#                       We're missing multiple in a row, so append a range
                        missingFrames.append(str(firstMissingFrame)+"-"+str(lastMissingFrame))
                        firstMissingFrame = None
                        lastMissingFrame = None
#                   Then move on
                    i += 1
#               If this isn't the last frame
                else:
#                   And the first isn't already set
                    if firstMissingFrame == None:
#                       Set it and move on
                        firstMissingFrame = frameRange[i]
                        i += 1
#                   Or the first was set
                    else:
#                       Set this as the last and move on
                        lastMissingFrame = frameRange[i]
                        i += 1