## Adding your page to the website
1. Create a new branch by executing `git checkout -b your_name_branch` in the terminal.
2. Add your name to `members.txt` under the appropriate category in alphabetic order by last name. Type your name _exactly_ how you would like it to show up in the directory.
3. Copy `members/example_student.md` to `members/your_name.md`, where `your_name` is the name you wrote in (1), but lowercase and with '_' instead of spaces.
4. Fill out `members/your_name.md`!
5. Add a professional photo (preferably square aspect ratio) at `assets/img/your_name.png`.
6. Add any extra photos (research, hobbies, etc.) at `assets/img/your_name_#.png`., where `#` is a number 1-3.
7. Run `make_member_page.py` and check that there are no errors.
8. Commit your branch and push it to the repository with `git add *; git commit -m "Making a page for your name"; git push origin your_name_branch`.
8. Create a pull request on `https://github.com/cersonsky-lab/website/pulls` and check that all tests run.
9. Request one of your group members and Rosy as a reviewer.    
