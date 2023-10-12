## Generate my GPG key
`gpg --full-generate-key`

## Show my GPG key
`gpg --list-secret-key --keyid-format LONG`

## Init Pass
`pass init <GPG KEY>`

## Add new password -> all files are stored at ".pawwrod-store/"
`pass insert twitter.com`

## decrypt
`gpg -d facebook.com.gpg`

## display password
`pass twitter`

## Copy to clipboard
`pass -c git_token`

## Remove passwords
`pass rm Business/cheese-whiz-factory`

