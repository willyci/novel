Chapter 7: The Professor

Sol 44 began the way the last three had — with a recycled-air taste at the back of Peter's throat, a left display flicker he had stopped logging, and the quiet, persistent fact that he could not make the project specs reconcile with anything he understood about asteroid mining.

Four mornings into the routine, his routine had a shape. He woke at 0530 in the small cabin assigned to him on the residential level, dressed in the standardized gray coverall with no visible affiliation, walked the curved corridor to the galley, drank coffee with a chemical undertone, and arrived at the Nav Lab by 0615 to find his workstation already humming where he had left it the night before. The military-grade software had not stopped processing while he slept; it ran perturbation simulations against epoch references he had not yet authorized, the way a well-trained dog continues a trick if you forget to release it. He had not asked who else, if anyone, watched the outputs. He had instead begun closing the same warning twice a day — a soft yellow flag from the integrator about reference-frame anachronism — and telling himself he would address it once the higher-level architecture made sense.

It had not made sense. He had stopped admitting that to himself by Sol 43. By Sol 44, the not-admitting had its own shape, too.

He had just sat down with his second coffee when Samir's voice came at his shoulder, easy and unannounced.

"Mr. Kamau. The project lead would like to meet you."

Peter looked up. Samir was already half-turned toward the corridor, already sure Peter would follow. There was something in the phrasing that caught Peter off the line — *the* project lead. Until that moment Peter had assumed Samir was the project lead, in the practical sense; he had signed Peter's contract, met the shuttle, given him the orientation. The presence of someone above Samir reorganized the small map Peter had been drawing of the base in his head.

He stood up. "Now?"

"Now," Samir said, in a tone that suggested *yes, now* but also *he is not the kind of man who makes you wait, and you should not make him wait either.* The smile was on for half a second and then off.

They went out into the corridor and turned left, away from the path Peter had walked four mornings in a row.

The base was bigger than what Peter had seen. He had known that abstractly — the asteroid was two kilometers along its longest axis, and the residential and Nav levels accounted for maybe a tenth of the warmed volume — but knowing a number was not the same as walking into it. Samir led him down a sloping passage with floor lights set into the rock, past a sealed pressure door labeled in plain stenciled type *MANUFACTURING — AUTHORIZED ONLY,* and then through a wider arterial corridor where the air carried the faint, sweet ozone of high-current machinery somewhere not far off.

They passed an open bay on the right and Peter slowed without meaning to.

The room was long and low-lit. Three programming stations faced inward toward what he first read as a fish tank and then, on second look, was not a fish tank: a clear-walled containment running the length of the room, full of a fine, settled medium that resembled gray flour, except that the surface of it moved in slow, patient ripples, as if something extremely small was breathing through it. A man sat at the nearest station, hunched, wearing fingerless gloves. On his terminal Peter caught a flicker of code — recursive constructors, replication clauses, the unmistakable nested syntax of self-replicating routines — before the angle changed. The man did not look up. With his free hand, he reached toward a small port in the containment wall and laid two fingertips against it, briefly, the way a parent presses a palm to a sleeping child's forehead. He withdrew his hand and resumed typing.

Peter kept walking. Samir had not slowed.

A few meters on, a side passage opened to the left, and a woman in a charcoal lab coat stepped out of it directly into Peter's path. They both stopped politely and he placed her in the same instant — the third name in his project sheet, *Dr. E. Vasquez, Accelerator Integration.*

"You're the navigation hire," she said. Not a question.

"Peter Kamau."

"Vasquez." She looked, for one second, at Samir, who nodded fractionally and continued past them, leaving Peter to her. "I won't keep you. I've sent you a parameter spec for the integration windows — I'll need timing tolerance below two milliseconds across the bus, and I want the accelerator's output frame referenced to your trajectory frame, not the other way. Read it before you commit any of your perturbation models. We've had problems with that before."

"Okay," Peter said. "What's the output bus rated at?"

"Higher than you'll need." There was a flicker — annoyance, maybe, or simply the impatience of someone whose mind was already five steps further on. "Read the spec. We'll talk."

She was past him before he finished nodding. He watched her go for half a second longer than he meant to. *Higher than you'll need* was not a thing accelerator engineers said about their own output bus. Accelerator engineers gave you a number, in joules, and watched you flinch.

Samir was waiting at a doorway twenty meters on. As Peter caught up, a young woman — short, tired-eyed, holding two paper cups of something dark — came out of a side door and threaded past them with a quick "Morning, Professor" called toward the open doorway behind her. She did not look at Peter at all.

Samir stepped aside. "He'll see you. I'll be in operations." And then, as a small kindness Peter would only register later: "Take your time."

Peter went in.

The office was not a startup CEO's office.

A startup CEO's office, in Peter's limited experience of Olympus glass towers, was a curated piece of theater: minimalist desk, single sculptural lamp, one carefully chosen book turned face out on a credenza. This room was the opposite. Three of its walls were lined with shelves, and the shelves held *paper books* — actual, physical books, several hundred of them, with the bowed spines and cracked cloth of objects that had been moved between locations and read more than once. The fourth wall held framed photographs, a dozen at least, all of them outdoor, terrestrial: a coral reef in shallow water lit from beneath, a strip of shoreline at low tide with three figures crouched over something Peter could not resolve, a jungle clearing at dusk, a survey camp pitched on a mossy slope. The man in the photographs, where he appeared, was always at the edge of the frame, always looking at the work and not at the camera.

A working terminal on the desk showed a half-rendered trajectory simulation — Peter recognized the integrator footprint, his own perturbation model running quietly in the corner — and beside the terminal, on the bare wood, was a single fragment of pale, branched coral, set on a small glass stand, no label, no plaque.

The man behind the desk rose. He was sixty, perhaps a little older, with iron-gray hair cropped close and the kind of physical economy that comes from having lived for a long time in places where you carried what you needed. His eyes were dark and unhurried. He came around the desk with one hand out.

"Peter. I've been reading your code all week. Sit, sit." He took Peter's hand briefly and warmly, then gestured to the chair across from the desk. "Coffee? It's barely worse than the galley's."

"I've had two already, sir."

"Arthur. Or Kessler, if you must. I'm trying to discourage 'sir' on this base. It hasn't taken." He smiled, and the smile was small, dry, and entirely real. "Tell me about the cluster you proposed for the perturbation reference frames. The one in the second commit yesterday afternoon. I have been arguing with my own integrator about it since 0400 this morning and I am, regrettably, persuaded."

Peter sat. He had not expected to be questioned about a code commit before he had been told what the code was for.

"It was a small thing," he said. "The reference frames you had me building against were each anchored independently. The integrator was carrying drift across them I didn't think it needed to. I clustered the nearer epochs against a single barycentric anchor and let the further ones float. It cuts compute by about a third and keeps the residual under tolerance."

"It does more than that," Kessler said. "It makes the failure mode legible. If the cluster shifts, you see it shift. If they're independent, you only see the integrator unhappy and you have to go find the reason." He sat back. The pleasure on his face was not performed; it was the quiet pleasure of a man who had been waiting, for longer than he wanted to say, to talk to someone who saw the same thing he saw. "That is exactly why we wanted you, Peter. Three other people looked at that architecture before you. None of them touched the anchors."

The warmth came up under Peter's ribs before he could intercept it. He had not been told he was good at his work in six months. He had told himself, in the mornings, that he did not need to be told. It turned out he had been lying about that the way he had been lying about the warning flag.

"Thank you," he said.

"I used to teach," Kessler said, almost to himself, looking at the trajectory simulation. "Students like you would have made my office hours bearable."

Peter filed it. He did not ask where, or what.

They talked for perhaps thirty minutes. Kessler asked about Helix, about the de-orbit work, about the six months after — gently, without the pity-curiosity of a hiring manager. He asked about Peter's grandfather's name, which was on Peter's resume for reasons Peter had never quite been able to articulate. He listened more than he spoke. When he did speak about the project, he used phrases that Peter found himself, later, trying to remember exactly: *deep time,* *epoch-true reference,* *operations on geological scales.* He used these phrases in the way other people said *quarterly* or *fiscal year* — as if they were the natural unit for the problem in front of him. Peter did not ask why.

When Peter rose to go, Kessler shook his hand again. "We'll have you over for dinner this week. The galley does us no favors but the company is decent."

"I'd like that."

"And Peter — " Kessler hesitated. The hesitation was small enough that Peter would not, later, be sure whether he had imagined it. "Anything you find in the code that does not make sense to you, bring it to me. Directly. Not to Samir. The code is mine, not his."

"Yes, sir."

"Arthur."

"Arthur."

Peter walked back to the Nav Lab through corridors he was beginning, in spite of himself, to recognize. He passed the bay with the gray-flour containment again. The man with the fingerless gloves was still typing. The surface of the medium still rippled, slowly, patiently, in the way of something extremely small and extremely awake.

At his workstation, Peter sat for a long time without opening anything.

Then he opened the project specs.

He went to the section on reference epochs. He had read it three times in four days. He read it again now. The tolerances had not changed. The nav code was required to maintain a stellar drift correction across reference frames spanning, in places, *millions of years.* Not a typo, not a units error — he had checked both. A cluster of nearer epochs anchored against the present, yes; but the integrator was specified to carry, gracefully, across an envelope that no commercial mining trajectory required and no trajectory in the catalogue of human spaceflight had ever needed. He had compartmentalized the parameter for four days under the working assumption that there was an explanation he had not yet been told. That assumption had been doing a great deal of work.

He thought about Kessler's hands when he had said *operations on geological scales.* He thought about the coral fragment on the desk. He thought about the way the man with the gloves had touched the containment wall.

He liked Arthur Kessler. That was the part he made himself look at directly.

He liked him, and he wanted the project to make sense, and these two things were not the same thing.

He took the small paper notepad from the drawer of the workstation — the kind of notepad that was almost an affectation in 2543, here for fire drills and nothing else — and wrote three lines, in the small, square print he used for things he did not want to lose:

*Why does the nav require stellar positions millions of years deep?*
*Whose mining trajectory has ever needed that?*
*Ask Arthur. Tomorrow morning. First thing.*

He read it twice. Then he turned the page over so that the writing faced the desk, and he set the notepad to the left of his keyboard, where his hand would find it without looking.

On the left display, the soft yellow warning flag flickered once, almost shyly, and resolved.
