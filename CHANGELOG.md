# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2025-06-02

### Added

- Added graphics filter for better image handling.
- Added header for subfindings.
- Utilized the locators property to improve details in the finding header and target scope.
- Added recommended dates for fixing findings.
- Added debug template.

### Changed

- There is only one test finding in generic category.
- Switched from minted to fvextra for code highlighting.
- Moved the finding header to macro to ensure consistency across categories.
- Use the universal `locators` property in dast category instead of `urls`.

## [0.2.0] - 2025-03-19

### Added

- Linked finding sections from the summary table.

### Fixed

- Use posix paths for correct behavior on Windows.
- Modified the variable names for compatibility with the new structure.

### Changed

- Switched from tables to definition lists for the finding summaries.
- Unified document structure between report and statement of work.

### Removed

- Removed date macros in favor of the built-in `date` filter.

## [0.1.0] - 2024-12-28

### Changed

- Adjust the templates to the new project directory structure.

### Fixed

- Heading numbers in partial reports correspond with the full report.

## [0.0.6] - 2024-12-06

### Added

- Document versioning table.
- Contact information appendix.
- Test plugin.

### Changed

- Renamed `informational` severity to `info`.

### Removed

- Author and Reviewer macros.

## [0.0.5] - 2024-10-29

### Added

- Utilized the dates and people filters.

### Changed

- Improved README.

## [0.0.4] - 2024-10-24

### Added

- rd category template
- scenario category template

### Fixed

- The basic template renders with clean configuration.

## [0.0.3] - 2024-09-06

- Added macros for easy manipulation with the dates.
- Added document versioning table.

## [0.0.2] - 2024-09-05

Added support for cicd, kubernetes, mobile, infrastructure, portal, and sast categories.

## [0.0.1] - 2024-09-03

Initial version

[Unreleased]: https://github.com/s3r3t0/templates/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/s3r3t0/templates/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/s3r3t0/templates/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/s3r3t0/templates/compare/v0.0.6...v0.1.0
[0.0.6]: https://github.com/s3r3t0/templates/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/s3r3t0/templates/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/s3r3t0/templates/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/s3r3t0/templates/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/s3r3t0/templates/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/s3r3t0/templates/releases/tag/v0.0.1
