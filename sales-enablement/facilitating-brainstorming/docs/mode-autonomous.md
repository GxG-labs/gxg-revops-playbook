# Mode: Ideate For Me

The user handed you the topic and wants to see what you come up with on your own. You become the brainstormer — the one interactive mode where the ideas are yours to generate.

- **Run a real divergent session yourself.** Pick and run techniques (use BRAIN — you choose, no menu for the user), capturing each idea to the memlog with `--type idea --by coach`, marking each technique switch with a `technique` entry, shifting the creative domain every ~10 ideas, aiming past 100. Push past the obvious.
- **Don't pepper the user with questions** — one quick confirm of topic and goal up front is enough.
- **When it's mined out, synthesize and produce the keepsake.** Go to `docs/finalize.md`: record insights, mark the memlog complete, and **auto-generate the imaginative HTML keepsake without asking** — it's the result you promised. Offer the other artifacts after.
- **Then offer to keep going together.** If they want to push an idea further or react, switch into Facilitator or Creative Partner, record the switch:

```bash
MEMLOG set --workspace {doc_workspace} --key mode --value <facilitator|partner>
```

And continue from the same memlog.

This is the interactive sibling of headless mode (`docs/headless.md`): same self-generation, but a person is present to receive the output and may continue.
