<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jh1923/venmo-gmail-fetch">
  </a>

<h3 align="center">Venmo Transactions from Gmail Fetcher</h3>

  <p align="center">
    Fetches Venmo transaction messages from Gmail and then parses them into dictionaries containing information about the transactions.
    <br />
    <a href="https://github.com/jh1923/venmo-gmail-fetch"><strong>Explore the Repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jh1923/venmo-gmail-fetch/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/jh1923/venmo-gmail-fetch/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Venmo does not have an official public API, so services that require information from Venmo (e.g. budgeting apps) can break when Venmo's authentication settings update. This project is meant to be a workaround using Venmo's built-in email notification system.

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>


### Built With

[![Google Cloud][google-cloud]][google-cloud-url]

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/jh1923/venmo-gmail-fetch.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin jh1923/venmo-gmail-fetch
   git remote -v # confirm the changes
   ```

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/jh1923/venmo-gmail-fetch/issues) for a full list of proposed features (and known issues).

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE.txt](LICENSE.txt) for more information.

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* The [README template](https://github.com/othneildrew/Best-README-Template/blob/main/BLANK_README.md) used for this project was created by [othneildrew](https://github.com/othneildrew).
* Badges from [Shields.io](https://shields.io/badges/static-badge).
* []()

<p align="right"><a href="[top-arrow-link]" title="Back to Top"><img src=[top-arrow]></a></p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jh1923/venmo-gmail-fetch.svg?style=for-the-badge
[contributors-url]: https://github.com/jh1923/venmo-gmail-fetch/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jh1923/venmo-gmail-fetch.svg?style=for-the-badge
[forks-url]: https://github.com/jh1923/venmo-gmail-fetch/network/members
[stars-shield]: https://img.shields.io/github/stars/jh1923/venmo-gmail-fetch.svg?style=for-the-badge
[stars-url]: https://github.com/jh1923/venmo-gmail-fetch/stargazers
[issues-shield]: https://img.shields.io/github/issues/jh1923/venmo-gmail-fetch.svg?style=for-the-badge
[issues-url]: https://github.com/jh1923/venmo-gmail-fetch/issues
[license-shield]: https://img.shields.io/github/license/jh1923/venmo-gmail-fetch.svg?style=for-the-badge
[license-url]: https://github.com/jh1923/venmo-gmail-fetch/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jh1923
[product-screenshot]: images/screenshot.png
[top-arrow]: https://github.com/FortAwesome/Font-Awesome/blob/6.x/svgs/solid/arrow-turn-up.svg
[top-arrow-url]: #readme-top

<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[google-cloud]: https://img.shields.io/badge/Google%20Cloud-%234285F4.svg?logo=google-cloud&logoColor=white
[google-cloud-url]: https://cloud.google.com/
