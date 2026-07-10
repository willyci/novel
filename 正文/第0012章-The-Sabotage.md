Chapter 12: The Sabotage

Peter had three places, and by the end of Sol 71 he had one.

He ran the elimination on the morning walk between his bunk and the Nav Lab, because a trade study that could never be written down had to be carried in the head, and carrying was easier while the body was doing something ordinary. The first place was the integrator's frame-priority table in the launch trajectory phase. He struck it off before the corridor's second bend. The table lived one layer beneath the cradle handshake, and everything within one layer of the cradle handshake had Vasquez's fingerprints in its diff history and Vasquez's timing regressions parked on top of it like a guard that did not sleep. A change there would be found, not because it was wrong, but because that was the neighborhood she watched. The second place was the thrust-allocation solver in the station-keeping loop. He struck it off at the Nav Lab door. The solver audited itself — a symmetric residual check, momentum in against momentum out, that the satellite would run once a second for three and a half thousand years — and a sign inversion there would fail physics, and physics was the one reviewer that could not be talked past, distracted, or made to run out of time on Sol 75 at 1700. What he needed was a place where the code could not check itself against the world.

What he needed was a convention.

The third place was the gravitational-parallax correction module in the deflection phase — interceptor approach geometry, in the language of the spec, the language he still used in his commit messages and would go on using. The module was small. Two hundred lines, most of them frame bookkeeping. During close station-keeping, the satellite would fix its position relative to the target body by parallax against Jupiter — the only lamp in the outer system bright enough and far enough to range on — and the correction it produced fed the approach geometry directly: which side of the target the satellite stationed itself on, and therefore which direction its mass pulled. The module's whole job was to take a bearing measured in the star tracker's frame, carry it through an inertial frame fixed by catalog match, and deliver it into the body frame as a correction vector. Three frames. Two transforms. Each transform a quaternion.

A quaternion is four numbers that promise a rotation. Flip the sign of one of the four and the promise is still, to every syntactic and dimensional check ever written, a rotation — of the mirror of the world. There is no experiment a piece of code can run inside its own frame to learn the handedness of that frame. Handedness is not a measurement. It is an agreement between two pieces of software, and an agreement can be misremembered by exactly one minus sign.

Applied where he was going to apply it, the mirror did one thing. It reflected the parallax correction across the approach plane, and the approach geometry, faithfully executing a correct maneuver on a mirrored input, would station the satellite on the far side of the target body — the side away from Jupiter. The push became a pull. Plus 0.01 degrees became minus 0.01. And the satellite would never learn what it had done, because the body it was flying formation with — ten kilometers of chondrite between its star tracker and the one lamp it ranged on — would occlude Jupiter for exactly as long as the error lived. The bug did not have to hide from the satellite forever. It only had to hide until the satellite's own position blinded it, and after that, orbital mechanics would do what orbital mechanics does, which is not forgive.

That was the place. The trigger took him the rest of Sol 71.

The trigger already existed, was the thing. He did not have to build it, only to lean on it. The parallax module carried two star catalogs, and this was legitimate, specified, reviewed architecture: a contemporary catalog for integration and test, and a reconstructed deep-epoch catalog — every star's proper motion run backward across sixty-seven million years — for flight. The module chose between them on one input only: the satellite's own star-field epoch verification, the measured positions of a few thousand stars matched against both catalogs, the offset solved for directly. Not the mission clock. He had heard the reasoning in a design note written before he was hired, and the reasoning was sound, and he had spent part of Sol 71 hating how sound it was: no clock could be carried through a Cauchy crossing with authority. The stars were the only timestamp the machine would ever be able to trust. So the code had been built to trust them, and once the maneuver began, it would believe its sensors over its parameters, over its clock, over anything a human had told it — because a human had told it to.

If the verified epoch offset ran deeper than sixty million years into the past, the deep-epoch regime engaged. Nowhere else. Not in any simulation, because the simulation harness's star-field synthesizer signed every frame it generated with the harness's own epoch — a shortcut somebody had taken years ago, because why would the harness lie about when it was running — and Peter had found that shortcut on Sol 66 and had been carrying it since the way a man carries a key he has not yet admitted fits a door. Not in any regression, not in Vasquez's review environment, not on any workstation on the base. There was no test that could be run in the present that would ever make the condition true. The condition was true in exactly one place, and that place was sixty-seven million years away.

He wrote it on Sol 72.

The work it rode in on was real. Deep-epoch catalog support hardening was on the schedule, his name against it, Vasquez's walkthrough five days out; he had a legitimate reason to touch every line of the module, and he touched every line. He rewrote the frame chain as a clean pair of adapters, contemporary and deep-epoch, four hundred and some lines of diff, most of it genuinely better than what it replaced. That was the part he had not been prepared for — that the camouflage had to be his best work, that the box he was hiding one poisoned line in had to be built so well that a rigorous reviewer would enjoy reading it. Inside the deep-epoch adapter's constructor, where the reconstructed catalog's frame convention was declared, one component of one quaternion carried a sign it should not have carried. The thirty-first character of the line. He typed it at 1410 on Sol 72 with the stellar position consistency check due to run against his branch nine minutes later, and it ran, and it passed, because a consistency check compares positions and a mirror preserves every distance it touches.

He read the line back once. It looked correct. That was the terror of it, the specific kind he would keep until Sol 80 and, he understood, past it: the line looked correct to him too. He had written a thing whose armed path he could never execute, never step through, never watch fail or succeed — a weapon that could not be test-fired, aimed at a target that would not exist for the purposes of any instrument he owned until the moment it worked or did not. He wrote the round-trip test anyway, transform and inverse transform, identity out for identity in, and it passed, and it proved nothing, and he knew it proved nothing. A round trip cannot detect a mirror. You go into the glass and you come back out and you are yourself again. The only thing that can detect a mirror is the world.

On Sol 73 Kessler found him in the galley at the end of the day shift and asked if he had an hour, and the hour was the gray-flour bay.

The man with the fingerless gloves brought the imaging feed up without being asked. Under the containment glass the medium lay the way it always lay, and out of it, held apart in a separate cell no wider than a hair, one machine. One micrometer. The screen's scale bar was longer than the machine was. Peter looked at the thing his code would ride in and found that it looked like nothing — a gray sphere, faintly faceted, a bacterium that someone had machined.

"Thirty-four billion atoms," Kessler said. "I have read the manifest so many times I dream in it. Blueprints, replication logic, your navigation stack — and eleven hundred spare bytes in dead storage, which the nano team wanted for checksums." He was smiling. He looked rested, which was new. "I overruled them. Ten names are in there, Peter. Everyone on this base, in a block the machine will copy forward into everything it ever builds. Ten billion years from now, whatever is left of what it makes will have us in it. I wanted you to see yours before it ships."

The feed's side pane held the dead-storage block, rendered as text. Peter read the ten names. His was seventh. He stood in the cool of the bay with the man who had put it there warm at his shoulder, and he made himself say the thing a man would say.

"You could have used the bytes."

"I have spent my life on things that used every byte." Kessler's eyes stayed on the machine in its cell. "Once — once — I am going to carry something that doesn't have to earn its mass." He put his hand flat on the containment glass, not gently, the way a man touches a hull. "Your work is the part of this I never have to check, do you know that? Vasquez checks it because Vasquez checks everything. I stopped checking in week three. Give her a clean build on Sol 75 and then sleep, because after lockdown, Peter, none of us can touch it. It has to be right the way a thing is right when you can never touch it again."

"It will be," Peter said, and it was the truest sentence he had spoken on the base, and it went through him like a blade going through, exactly as cold, exactly as clean.

That night he wrote the second thing.

It was small and it was his and no one had asked for it. The satellite's long-range telemetry beacon — catch-status reporting, in the language of the spec — opened every frame with a synchronization preamble, a pattern whose only requirement was that it be improbable, and a reserved padding block that the format had carried since before Peter was hired because deleting fields from a frozen format is more dangerous than feeding them constants. Preamble constants and padding words are the two things no reviewer in the history of reviewers has ever questioned. He patterned the preamble's pulse intervals on the primes — two, three, five, seven, on upward, the one sequence no process in nature produces and every mathematician in any possible audience recognizes — and into the padding, encoded so that the primes themselves taught you how to read it, he put a record. Not an apology. A record. His name. The line, and where it lived, and what it did. Why. That he had not been able to think of a cleaner door out of the world than the one he was closing, and that if anyone, anywhen, was hearing this, they were hearing it because a machine his species built was still faithfully repeating the confession of the man who had broken it — and that he hoped whoever they were, they had a sky they were fond of.

Kessler had put ten names in the seed. Peter put in the eleventh thing. The beacon would say it as long as the satellite lived, a few bits per frame, a whisper under a whisper, sixty-seven million years long. He signed nothing else in his life. He signed that.

Sol 74 he ran regressions and ate paste. The full suite went green in four hours eleven minutes, every present-day epoch stamp steering every test harmlessly down the contemporary path, the dormant branch dormant, the way it would stay dormant through every check the base could ever run. Samir stopped at his console in the afternoon — Samir, who had hired him, who the project had folded politely around and past — and stood reading over his shoulder for a while, which Samir was allowed to do and almost never did.

"I read your adapter rewrite last night," Samir said. "I don't get to sign off on anything anymore, so take this for what it costs, which is nothing. It's the best code on this base."

"Thank you," Peter said, to the man looking directly at the mirror and seeing a window, and Samir nodded and went to get coffee.

Sol 75, 1400, the integration room. Vasquez with two displays and his branch checked out read-only, three hours blocked, the walkthrough she had promised him: launch trajectory phase, cradle handshake, interceptor approach geometry, end to end, no surprises on Sol 80.

She was better than he had let himself remember. She did not read code the way programmers read code, top to bottom, trusting the story. She read it the way she read her accelerator — pick a value, follow it through the machine, make the machine justify itself at every flange. She followed a timing offset through the handshake and made him say out loud where every microsecond went. She opened the deflection phase at 1602.

At 1619 her cursor stopped on the epoch gate, and she leaned back, and she asked the question.

"Why does a parallax correction care what year it is?"

The room stayed the size it had been. He gave her the answer, which had the advantage of being true. Sixty-seven million years of proper motion; a star field that would not match any contemporary catalog by whole degrees; two catalogs, two adapters, and a gate. And the gate ran on the verified epoch, not the mission clock, because no clock crossed a Cauchy horizon with authority — the stars were the only timestamp the machine could trust, so the machine had been built to trust them over everything, including us.

Vasquez looked at the gate for a count of seconds.

"Sensors over assumptions," she said. "If my accelerator disagreed with my model, I'd believe the accelerator." She pulled the deep-epoch adapter up and scrolled it once, top to bottom, and her cursor passed the constructor, and passed the line, and rested two lines below it on the round-trip test. "Transform validation. Against what truth?"

"Round trip. Forward through the adapter, back through its inverse, identity within numerical noise."

"Self-consistency," she said, in the flat voice she used for things she was deciding whether to accept, and for one count Peter watched her stand at the edge of the only question that mattered — a round trip proves the glass is smooth, it does not prove it isn't a mirror; the words existed; she was one thought away from them — and then she said, "It's the correct test for a convention. Conventions don't have a truth. They have an agreement," and scrolled on, and the mirror sat there in her display, agreed with.

At 1655 she ran the full suite live from her own environment, and they watched it go green together, and it was very quiet in the integration room, and Peter's face did what his face had been doing since Sol 66, which was its job.

At 1712 she signed the build. She read the hash aloud, the first eight characters, the way she read her beam energies, and he confirmed them against his display, and she committed the lockdown, and somewhere in the base's core a repository went immutable, and the code that would run for a million years, and the minus sign in it, and the primes under the padding, all of it stopped being something anyone alive could touch.

"Clean build, Kamau," Vasquez said. "You're the one interface on this project I never have to fight."

He walked back through the day-cycle corridors, past the gray-flour bay, where the door was open and the seed sat in its cell being nothing to the naked eye. At his workstation the screen corner was blank, and he looked at the blank for the count it always took, and then he did the close-of-day.

The build was clean. She had used the right word. Every line in it did exactly what he had written it to do.
