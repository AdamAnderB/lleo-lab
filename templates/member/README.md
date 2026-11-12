# Add a consenting member
Copy the structure below into the members.json list, replacing every placeholder. Use a unique lowercase slug; links are optional and can include a personal site, GitHub, CV, or outputs. Confirm text and visibility with the member first. Never publish this example as a real person.

```json
{"slug":"chosen-name","name":"Chosen display name","role":"Confirmed role","public":false,"bio":"Approved short research bio.","links":{"Personal website":"https://example.org/"}}
```
Set public to true only after consent. Run `python3 build.py` and `python3 check.py`. Check the profile and People listing. Add specific project connections in build.py as needed. For alumni or collaborators, explicitly identify that status in the role.
