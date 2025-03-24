# Changelog

## v0.6.1 (2025-03-24)

### Bug fixes

- Strip quotes from file and folder paths in main.py input handling ([`4cbb058`](https://github.com/markm-io/dataslicer/commit/4cbb05861828195070a1b1d33673eee6298f4ac2))

## v0.6.0 (2025-03-21)

### Features

- Enhance file input handling to support directories and ensure consistent columns across multiple files ([`ff84ed7`](https://github.com/markm-io/dataslicer/commit/ff84ed7dbcd7f03f9621733e9c4d6ed15b235efa))

## v0.5.0 (2025-03-21)

### Features

- Allow custom string input for filename selection in main.py ([`ee6eb3b`](https://github.com/markm-io/dataslicer/commit/ee6eb3b1415e8b44e0fa29cb4f7afa5249046fb1))

## v0.4.1 (2025-03-21)

## v0.4.0 (2025-03-21)

### Bug fixes

- Update sed command for macos icon assignment in ci.yml ([`ec9b0dc`](https://github.com/markm-io/dataslicer/commit/ec9b0dc71a877526699e6564aac45db8099b1c82))

### Features

- Add icon to executable ([`fb2be92`](https://github.com/markm-io/dataslicer/commit/fb2be925cb4f0b8723c335ff49a4f5934be5d655))

## v0.3.0 (2025-03-19)

### Features

- Add filename column selection and update export logic in main.py ([`2d709db`](https://github.com/markm-io/dataslicer/commit/2d709dbe947f37701cb808749947e61c2e4031fd))

## v0.2.14 (2025-03-19)

### Bug fixes

- Update indentation size to 4 and improve filename sanitization in main.py ([`a8c2bf8`](https://github.com/markm-io/dataslicer/commit/a8c2bf896040cd61b849a219d6cd60bc82aeb20d))

## v0.2.13 (2025-03-19)

### Bug fixes

- Replace custom filesystem sanitization with pathvalidate library functions ([`04486ef`](https://github.com/markm-io/dataslicer/commit/04486ef7eedcb97b4358d138ae01e570a2c80c9c))

## v0.2.12 (2025-03-19)

### Bug fixes

- Improve filename and folder sanitization logic in filesystem handling ([`e5a2fd9`](https://github.com/markm-io/dataslicer/commit/e5a2fd922a2441a54bfe500abcf5c2b947dc9d55))

## v0.2.11 (2025-03-19)

### Bug fixes

- Bump version to 0.2.10 and update changelog ([`e1efca3`](https://github.com/markm-io/dataslicer/commit/e1efca382072fbbea0a2908ec1b9b5c3ecba4b4b))

## v0.2.10 (2025-03-19)

### Bug fixes

- Add platform-specific icon handling in dataslicer.spec ([`257344c`](https://github.com/markm-io/dataslicer/commit/257344c5f51e6c6e3ae997b39c3cc173258baa9c))
- Update codespell configuration and add dataslicer.spec for packaging ([`a6aaa8c`](https://github.com/markm-io/dataslicer/commit/a6aaa8cf3b032b8081671d9136f0f2bf67c984ac))

## v0.2.9 (2025-03-19)

### Bug fixes

- Enhance ci configuration to dynamically find and rename executables based on os ([`e6b26be`](https://github.com/markm-io/dataslicer/commit/e6b26be7af51f48fb7a19d5be13bb5d3f4a5b60f))

## v0.2.8 (2025-03-19)

### Bug fixes

- Update .gitignore to ignore all spec files except dataslicer.spec ([`1726ffb`](https://github.com/markm-io/dataslicer/commit/1726ffbcc80e6f6837acbf85741b7db6f6cbd02b))

## v0.2.7 (2025-03-19)

### Bug fixes

- Update ci configuration to remove unused os options and streamline executable naming ([`187dca2`](https://github.com/markm-io/dataslicer/commit/187dca2a35a728612bb6ecc99f0cb2687fc7a72d))

## v0.2.6 (2025-03-19)

### Bug fixes

- Refactor ci configuration to create a flat directory for executables and improve file verification ([`556001d`](https://github.com/markm-io/dataslicer/commit/556001d8042606d760524805dd1bd2bef47cf843))

## v0.2.5 (2025-03-19)

### Bug fixes

- Update ci configuration to use matrix strategy for os selection ([`0df190e`](https://github.com/markm-io/dataslicer/commit/0df190e030e7ad10042e9c740b027cd15bcc60f0))

## v0.2.4 (2025-03-19)

### Bug fixes

- Enhance ci configuration to list files, move executables, and verify final structure before upload ([`e8f76ae`](https://github.com/markm-io/dataslicer/commit/e8f76ae17d61e6871a3a87f5a30e1d4f9eaf2b6f))

## v0.2.3 (2025-03-19)

### Bug fixes

- Update executable naming and upload process in ci configuration ([`70edeef`](https://github.com/markm-io/dataslicer/commit/70edeef6034d98f0dea4c82ed4ff06f1e5f2d4fa))

## v0.2.2 (2025-03-19)

### Bug fixes

- Update package name in installation instructions and readme, add permissions to ci job ([`716af41`](https://github.com/markm-io/dataslicer/commit/716af415f148ea90e4c489ca672440bfd8ad5c87))

## v0.2.1 (2025-03-19)

### Bug fixes

- Update upload_executables job dependencies to include release ([`59fd818`](https://github.com/markm-io/dataslicer/commit/59fd8184e7ace6d69bd95503c25fd0765d6b6cd5))
- Update indentation size to 2 and enhance executable build process for different os ([`1839387`](https://github.com/markm-io/dataslicer/commit/18393872272e4f914cab1d909375edae173293ab))

## v0.2.0 (2025-03-19)

### Features

- Enhance user interaction with rich console prompts and messages ([`54c7fd0`](https://github.com/markm-io/dataslicer/commit/54c7fd05c70008e128f3803713eaaa5004eea3c4))

## v0.1.3 (2025-03-19)

### Bug fixes

- Update upload-artifact action to version 4 ([`66d595d`](https://github.com/markm-io/dataslicer/commit/66d595d63da034d8b32adb4134bfd484435db571))

## v0.1.2 (2025-03-19)

### Bug fixes

- Remove column selection printout from user prompt ([`2ace1c6`](https://github.com/markm-io/dataslicer/commit/2ace1c638aa20ad3f534b585725aab72958ef5b4))

## v0.1.1 (2025-03-19)

## v0.1.0 (2025-03-19)

### Bug fixes

- Rename project from 'dataslicer' to 'data-slice' and update python requirement ([`6f95935`](https://github.com/markm-io/dataslicer/commit/6f959358450b835d5e217967377b68ccae9c0f5a))

### Features

- Implement file handling and export functionality for excel and csv ([`c0e2eaa`](https://github.com/markm-io/dataslicer/commit/c0e2eaac6bbaa2b8d99a298444db1b2a44d5581b))
- Add openpyxl and pandas dependencies with version specifications ([`857a97c`](https://github.com/markm-io/dataslicer/commit/857a97c6ea47115a177f7458d02f77df7a6525a5))

## v0.0.0 (2025-03-19)

### Documentation

- Add @markm-io as a contributor ([`f931875`](https://github.com/markm-io/dataslicer/commit/f931875349608e0570134fe3406ec6e31f579b2b))
