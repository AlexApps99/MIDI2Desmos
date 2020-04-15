# MIDI 2 Desmos

## Program Usage
Make sure you have installed the python library `mido` from PIP before using this!

`python3 graph.py [file] [midi channel] [# of midi events] [semitones to transpose, + or -]`
| Term | Explanation |
| - | - |
| `file` | The location of the MIDI file to be processed |
| `midi channel` | The channel of the MIDI file to be processed |
| `# of midi events` | How many MIDI events to be processed before stopping |
| `semitones to transpose` | Set this number accordingly so the song is in range of the graph |

### Examples
`python3 graph.py examples/allstar.mid 1 125 19`
`python3 graph.py examples/astley.mid 4 125 13`

## Desmos Playback
1. In graph settings, make sure both the X and Y scale are 0 to 100 exactly
2. Make sure during this process you do not zoom in or out, pan around or do anything to affect the scale
3. Paste the output of this program into a formula cell
4. Select the formula onscreen so it is highlighted
5. Enable Audio Trace with `Alt-T`, on mac `Option-T`
6. Set the tempo with `Alt-(1-5)`, on mac `Option-(1-5)`
7. Finally, playback with `H`.


## How?
https://www.desmos.com/accessibility#audio-trace

## Examples
[All Star I](https://www.desmos.com/calculator/ve3erfwyxl)
[All Star II](https://www.desmos.com/calculator/rhti49tgkg)
[Misc. songs](https://www.desmos.com/calculator/fu2s0jmc35)

## PRs
Pull Requests are **highly encouraged**! This was quickly hacked together by me
and any improvements would be a welcome addition to this project.
