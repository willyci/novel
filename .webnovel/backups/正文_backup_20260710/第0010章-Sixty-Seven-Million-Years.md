Chapter 10: Sixty-Seven Million Years

The progress bar was at four percent.

Peter sat in the same chair he had been sitting in when he had opened the comparison tool, in the same Nav Lab where the warning flag used to live, and watched the bar move once in the count of a minute. He did the math the way a navigation programmer does the math — payload, throughput, density of the catalogue he had loaded onto the eight-year-old datapad — and arrived at a number he had already half-known when he hit *query*. The catalogue was denser than he had remembered. The query was specific. It would not finish tonight. It would not finish in two nights. It would batch, against a system that ran a stellar position consistency check on his branch every twelve minutes whether anyone was looking at the result or not.

He could not sit at the workstation watching it move. That would be the kind of thing a man did when he wanted to be noticed.

He let the bar run. He logged out of the comparison-tool pane, left the bar to its background process, walked back to his bunk through corridors that were already past midnight, and did not sleep well.

The next seven days went like this. Sol 59, the integration window with Vasquez. Cradle handshake under tolerance, sub-2ms across the bus, output frame referenced to his trajectory frame. She read his timing offsets, took two of them, sent the third back with a one-line comment. They did not look at each other any longer than the work required. Sol 60, eighteen percent. Sol 61, a galley meal he did not remember eating. Forty-one percent. Sol 62, sixty-seven. Sol 63, eighty-eight. He stopped at the Nav Lab at the end of each shift, gave the bar a count of ten seconds, and went to bed. He did not reopen the result pane. He did not look at the catch-side trajectory file. He performed catch-side-pass-1's last refactor, the one Kessler had said would clear the integration window, and on Sol 65 night, the bar was at one hundred percent.

He waited until Sol 66 to look at it.

The corridor at 0220 on Sol 66 night was the dimmed cycle, the recyclers running quieter, the gray-flour bay door shut. He walked it the way he walked it on the morning of his interview shuttle, without hurry, and let himself into the Nav Lab through the door that had no lock because nothing on the base had locks. He sat down at the workstation. The bar was where he had left it. Below the bar, a single result line.

Reference epoch barycentric center. Catalogue match: tag, epoch number, named-event field.

Peter read the line. Read it again. Set one hand flat on the desk because the desk was the closest solid object. Read it a third time.

Sixty-seven million years.

Not millions. Sixty-seven million. The Cretaceous.

He sat with it for a count of seconds he later would not remember the length of. He did not push back from the chair. He did not exhale audibly. He ran the query a second time, against a different catalogue's hash, with the reference frame inverted and the epoch metadata stripped from the input. The query took eleven minutes. The answer was the same. He ran it a third time, naively, with no preprocessing, the way a man with a corrupted datapad would run it to disprove the corruption. Same.

The named-event field was populated this time. He looked at it the way one looks at a stranger waiting in one's apartment.

He did not say no. The first private no was not spoken; it was the small dry interior fact of having read the result and not having been able to disbelieve it on the third pass. He closed the result pane. He left the comparison tool open. He needed to look at the trajectory file before he believed any of this, and he did not yet believe any of this.

He pulled the trajectory target geometry file out of catch-side-pass-1.

It was the file Kessler had walked him through on Sol 50, the second half of the spec — the half Peter had read for the first time that afternoon, with Kessler's voice still in the room, and called *interceptor approach geometry* in his own commit messages because that was what the spec called it. He had been coding against it for sixteen days.

He ran the geometry the other way.

In the spec frame, the trajectory was the inbound path of an ancient ingot arriving on a present-day catch envelope after a million-year ballistic flight. Vector A, vector B, vector C, the catch-corridor calculated against Jupiter's chaos horizon, the integration tolerance Vasquez had called higher than he'd need. He had been integrating the catch-corridor against the present-day station-keeping mesh of the orbital interceptors Kessler had named. *Distributed. Several inner-Kuiper, several near-Earth. A handful on solar-orbit station-keeping at L4 and L5.*

He inverted the frame.

In the inverted frame, the same vectors became the approach path of a single body, falling on Earth. The same catch-corridor became the deflection envelope of an object in close station-keeping with that body, applying small thrust over the duration of the ballistic. Same math. The integration tolerance was the headroom for the Casimir cradle holding the Cauchy horizon open. The accelerator headroom Vasquez had said was higher than he'd need was higher than he'd need *for a Kuiper-Belt mining trajectory*. It was exactly what he'd need to inject a tenth-of-a-gram payload into a closed timelike curve at the moment of geodesic alignment with a sixty-five-million-year-prior earth-crossing orbit.

Peter sat with the geometry on his left display and ran a small recomputation in his head.

The 0.01-degree adjustment.

In the spec frame, 0.01 degrees was the launch-side tolerance — a tiny tweak applied at injection, governing whether the seed nanomachine landed on the correct gravitational anchor for von Neumann replication. Standard launch correction. Tiny.

In the corrected frame, 0.01 degrees applied to a body in close station-keeping with an asteroid, integrated over thousands of years of close orbit, was the deflection that made the asteroid miss Earth.

The 0.01-degree adjustment was not a launch correction. It was the entire point of his code.

He looked at the named-event field on the catalogue line. The metadata was tagged: *Chicxulub.* Then the impact-vector specification, generated automatically from the catalogue's reconstructed pre-impact orbit. The vectors in the metadata field were, within tolerance, the vectors in his catch-side-pass-1 trajectory target.

There were no orbital interceptors. There never had been.

He did not say it aloud. He thought it once, in his head, without verbs — *not mining*. The verb assembled itself a second later, of its own weight: *missing the asteroid on purpose.*

The implication landed in two stages. He held the first one — *the impactor never falls* — long enough to feel his hand cool against the desk. The second one arrived without ceremony, in the way of all conclusions a man's expertise has already done the work for and is simply waiting to deliver. If the asteroid missed, the dinosaurs survived. Mammals did not rise into the niches the impact had cleared for them. Humanity never evolved. The sixty-seven million years between the Cretaceous and the present did not produce the species that had built the solar economy, the species that had defunded Arthur Kessler, the species that had killed the Andaman Fragment. There were no humans to be. The plan was the ablation of his own species at its origin.

He sat with that for the count it took to read the sentence again, the catalogue line still on the display, the impact-vector field still glowing in the metadata column the way an answer glows when one stops being able to argue with it.

The corridor outside had started its day cycle. The strip-light shifted. Peter had not slept. He closed the trajectory file. He had to be at Vasquez's integration room in two hours. He had not yet decided what his face would do.

He went.

On the morning of Sol 67 he answered Vasquez's questions about the cradle handshake timing in cradle-handshake-timing language. The phase variance from the previous run had drifted by a margin he had to look up, and looking it up — opening a routine reference, glancing at a number, closing it — was the easiest professional act of his life because it was a single small task he could put his whole attention on without noticing the size of what he was carrying. Vasquez asked whether the integrator had complained about the new anchor cluster overnight. He said no, the residuals had stayed under tolerance, the cluster was clean. She nodded once and made a note. She asked, then, whether he could push the timing tolerance another half-millisecond before the next handshake, because the cradle was running cooler than the model and she wanted to spend the headroom. He said yes. He would have it for her by tomorrow. She did not look at him for any longer than the work required. The corner of her mouth did not do the almost-smile thing today. She was focused. He passed through.

He took a galley meal at midday. Oren was at the long table, halfway through a bowl of the unimpressive stew, and said, between mouthfuls, "Kamau. You look like you've been arguing with the integrator overnight."

"The integrator's been winning."

"They always do at four in the morning. Sleep."

"I will."

He would not. He ate. The stew tasted the same as it had on Sol 58 — the same dehydrated paste, the same recycler-air aftertaste, the same long galley table with the bench Oren had begun saving him a seat at without ever mentioning the saving — and he understood, with the small interior precision he had been bringing to all of his observations for the past day, that the saving was now the cage. Oren did not know the cage was a cage. Vasquez did not know it. None of them knew. He answered the words a man would say. He left the galley.

Back at the Nav Lab, late afternoon, he sat with what he had and did not touch the code. He thought about the photograph on Kessler's desk, lit from beneath — the reef in shallow water with the underlight that had lived in his head all week as a kind of warmth, and that lived in his head now as the recorded last image of a thing the man across the desk had decided to give the world back by removing the people who had taken it. He thought about the coral fragment on its glass stand.

The coral fragment was not a memento of loss. The coral fragment was the engine. The grief had been real — Kessler had not lied to him on Sol 58. Kessler had sat across from him and given him the truth about himself, all of it: the reef that died, the grandmother who had told him about a sea where the water was alive, the wife who had left, the basement lab in Tharsis Industrial. Every word of it had been true. None of it had been a confession. *I spent my life watching humanity destroy the most beautiful thing in the universe. This project is my chance to build something instead.* The line returned, exactly as Kessler had said it. Build something. Build a planet humans were never on.

The grief made the man. The man made the plan. Both were true. Peter understood, in the small disordered way one understands these things, that he had been sitting across from a man who had decided humans were the extinction event and was taking the appropriate measure.

For two short sentences, Peter let himself remember that on Sol 58 he had sat in that office and seen Kessler as a possible future self. He did not finish the thought. He did not need to.

He stood up to refill his water bottle. He walked the corridor to the dispenser. On the way back he passed Kessler's office. The door was closed. A strip of warm light showed beneath it. Inside, the man at the desk was preparing the third thing to tell him, the *third thing soon* that Kessler had laid down on Sol 58 like a key turned in a lock with one quarter turn remaining.

Peter walked past.

He returned to the Nav Lab one last time at 0140 on Sol 68. He sat down at the workstation. He closed the comparison tool. He opened the terminal cache and deleted his analysis — the query history, the back-derived trajectory file, the catalogue lookup logs, the runtime artifacts the comparison tool had written to a tmp directory under his account that nothing on the base would have flagged, because nothing on the base flagged anything Peter touched. He left catch-side-pass-1 untouched. He had not decided to do anything. What he was deleting was evidence that he had looked, not evidence of action.

The screen corner where the warning flag used to live, and where the progress bar had lived for eight days, was now blank. He looked at it for one count, the way a man looks at a place where a small light he had stopped noticing has gone out, and then he stood up and walked back to his bunk through corridors that hummed with sleeping recyclers. The gray-flour bay door was closed. He passed it without slowing.

His bunk was at the residential level. He turned the cabin light to its lowest setting, lay down on his back, and looked up.

The small observation port set high in the asteroid wall showed a wedge of stars. The actual stars of the present moment, in their actual positions. Sol 68 stars. Vega and the bright pair of Alpha Centauri and the long faint smear of the Milky Way at the angle Peter had gotten used to over six weeks of looking up at it on nights he was not sleeping. The Pleiades just out of frame to the left, where they always were.

The stars were exactly where they should be. For now.

He had the knowledge. He had the access. He had the one skill — the only one — that could stop the plan. The conditional was simple. He was not even going to think it as a line of code, not tonight; he had practice in not admitting what he had been doing, eight days of practice, and he knew how to apply it to himself. He let the unwritten conditional stay unwritten. He let it be the shape of a thing in the next room.

He did not have the certainty.

Not yet.
