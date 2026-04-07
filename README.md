<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/general_assets/pensiveeagle-logo-green.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">Weather Forecast Dashboard</h3>

  <p align="center">
    A small web app to display weather data on a dashboard, using Streamlit
    <br />
  <!--  <a href="https://github.com/PensiveEagle/weather-forecast-dashboard"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  <!--  <a href="https://github.com/PensiveEagle/weather-forecast-dashboard">View Demo</a>
    &middot;
    <a href="https://github.com/PensiveEagle/weather-forecast-dashboard/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/PensiveEagle/weather-forecast-dashboard/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is a learning project that aims to create a weather forecast dashboard app using Python and Streamlit. It sources data from an API to provide weather data for the upcoming days and then presents that back to the user through various views.

<img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/weather-forecast-dashboard/app_screenshot.png" alt="project_capture" width="100%" height="auto">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Docker][docker-shield]][docker-url]
[![Streamlit][streamlit-shield]][streamlit-url]
[![Python][python-shield]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* <a href="https://docs.docker.com/engine/install/" target="_blank">Docker</a>

### Installation

1. Get an API key from <a href="https://www.visualcrossing.com/sign-up/" target="_blank">Visual Crossing</a>
2. Clone the repo
   ```sh
   git clone https://github.com/PensiveEagle/weather-forecast-dashboard.git
   ```
3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin PensiveEagle/weather-forecast-dashboard
   git remote -v # confirm the changes
   ```
5. Rename .env_template to .env and add your API key to the file
4. Build the docker image
   ```sh
   docker build -t weather-forecast-dash .
   ```
5. Run the docker container
   ```sh
   docker run --rm -d -p 5005:5005 --env-file ./.env --name weather-dash-1 weather-forecast-dash
   ```


6. To stop the application
   ```sh
   docker stop weather-dash-1
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use the app navigate to http://localhost:5005

1. Make your location selection, the default is "London"
2. Select how many days you want to see the forecast for. Minimum of 1 and maximum of 5, default is 3.
3. Select the view you'd like. Only temperature is currently developed
4. Select your chart type
<img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/weather-forecast-dashboard/1-2-3-4_steps_screenshot.png" alt="project_capture" width="100%" height="auto">
5. View your forecast
<img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/weather-forecast-dashboard/5_steps_screenshot.png" alt="project_capture" width="100%" height="auto">


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

As there is a learning project there are a few features left unfinished, so I can move on to learning other techniques. Below is a list of features that could be added to improve this project:

- [ ] Add sky chart functionality that shows the sky conditions for each hour of the forecast
- [ ] Add error handling

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python Mega Course: Build 20 Real-World Apps and AI Agents - Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PensiveEagle/weather-forecast-dashboard.svg?style=for-the-badge
[contributors-url]: https://github.com/PensiveEagle/weather-forecast-dashboard/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PensiveEagle/weather-forecast-dashboard.svg?style=for-the-badge
[forks-url]: https://github.com/PensiveEagle/weather-forecast-dashboard/network/members
[stars-shield]: https://img.shields.io/github/stars/PensiveEagle/weather-forecast-dashboard.svg?style=for-the-badge
[stars-url]: https://github.com/PensiveEagle/weather-forecast-dashboard/stargazers
[issues-shield]: https://img.shields.io/github/issues/PensiveEagle/weather-forecast-dashboard.svg?style=for-the-badge
[issues-url]: https://github.com/PensiveEagle/weather-forecast-dashboard/issues
[license-shield]: https://img.shields.io/github/license/PensiveEagle/weather-forecast-dashboard.svg?style=for-the-badge
[license-url]: https://github.com/PensiveEagle/weather-forecast-dashboard/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jameshall-profile
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[kubernetes-shield]: https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white
[kubernetes-url]: https://kubernetes.io/
[docker-shield]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[streamlit-shield]: https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlit-url]: https://streamlit.io/
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/
[gradio-shield]: https://img.shields.io/badge/gradio-F97316?style=for-the-badge&logo=gradio&logoColor=white
[gradio-url]: https://www.gradio.app/
[flask-shield]: https://img.shields.io/badge/flask-3BABC3?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/stable/

