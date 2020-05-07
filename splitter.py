with open('all.md', 'r') as f:
    contents = f.read().split('\n-----\n')

for i, page in enumerate(contents, start=1):
    # get the line that the title is on
    title = page.split('\n')[1]

    # use lowercase
    title = title.lower()

    # get rid of spaces
    title = title.replace(' ', '-')

    page = '\n'.join(page.split('\n')[3:])

    # write the page to a file
    with open('tmp/{:03d}-{}.md'.format(i, title), 'w') as f:
        f.write(page)

# pandoc LessonsElectronicsandCS.html -o all.md -f html-native_divs-native_spans-raw_html-auto_identifiers -t gfm-raw_html-auto_identifiers --wrap=none
