import re

with open('all.md', 'r') as f:
    contents = f.read().split('\n-----\n')

for i, page in enumerate(contents, start=1):
    # get the line that the title is on
    title = page.split('\n')[1]

    # use lowercase
    title = title.lower()

    # get rid of spaces and format as filename base
    fname = '{:03d}-{}'.format(i, title.replace(' ', '-'))
    print(fname)

    # Get rid of the first few lines with the weird title
    page = '\n'.join(page.split('\n')[3:])

    # Demote all of the h1's to h2's to avoid showing up as pages
    page = re.sub(r'^# ', '## ', page, flags=re.MULTILINE)

    # write the page to a file
    with open('docs/{}.md'.format(fname), 'w') as f:
        f.write('# {}\n\n'.format(title.title()))
        f.write(page)

# pandoc LessonsElectronicsandCS.html -o all.md -f html-native_divs-native_spans-raw_html-auto_identifiers -t gfm-raw_html-auto_identifiers --wrap=none

# Convert all to rst
# for f in *.md ; do pandoc -s $f -o ${f%.*}.rst ; done ; rm *.md
