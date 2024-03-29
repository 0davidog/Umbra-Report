# Umbra Report Project Test File

## Table of contents

- [Umbra Report Project Test File](#umbra-report-project-test-file)
  - [Manual Testing](#manual-testing)
  - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
    - [Windows laptop](#windows-laptop)
    - [Chrome Emulated Device Dimensions](#chrome-emulated-device-dimensions)
    - [Browserstack Devices](#browserstack-devices)
    - [Market Share insights](#market-share-insights)
  - [Accessibility Testing](#accessibility-testing)
    - [Accessibility Audits](#accessibility-audits)
      - [Performance, Accessibility, Best Practices and SEO](#performance-accessibility-best-practices-and-seo)
    - [Keyboard Navigation](#keyboard-navigation)
  - [Validation Testing](#validation-testing)
    - [CSS Validation](#css-validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
  - [Automated Testing](#automated-testing)
  - [Defects](#defects)
  - [Defects of Note](#defects-of-note)
  - [Outstanding Defects](#outstanding-defects)

## Manual Testing

Manual testing was done for each completed user story and screenshots added to the comments on each issue page.

|User Story|Results|Detail|
|----------|-------|-------------|
|As a Site User, I want to register an account on the blog website so that I can create and manage my own posts.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/1)|
|As a Site User, I want to log in to the website securely using my credentials so that I can participate in the blog’s features.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/2)|
|As a Site user, I want the option to reset my password in case I forget it, ensuring secure access to my account.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/3)|
|As a Site User, I want to create a new blog post with a title, content, and optional images, so that I can share my thoughts and experiences.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/4)|
|As a Site User, I want the ability to update my existing blog posts to update or improve the content over time.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/5)|
|As a Site User, I want to be able to delete my own blog posts if I decide to remove them from the website.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/6)|
|As a Site User or Admin, I can create draft posts so that I can finish writing the content later.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/7)|
|As a Site Admin I can manage all blog posts through the admin panel to maintain control over the site’s content.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/8)|
|As a Site User I can view a paginated list of posts so that I can select which post I’m interested in viewing.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/9)|
|As a Site User, I can click on a post so that I can view the complete content.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/10)|
|As a Site User or Admin, I can view the comments on each individual post so that I can read the conversation.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/11)|
|As a Site User, I want to be able to comment on blog posts to engage with the author and other readers.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/12)|
|As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/13)|
|As a Site User, I want to be able to like blog posts to engage with the author and other readers.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/14)|
|As a Site User, I want a user-friendly navigation menu that helps me explore different sections of the blog easily.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/17)|
|As a Site User, I want the blog website to be responsive, ensuring a seamless experience on various devices, including desktops, tablets, and smartphones.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/18)|
|As a Site User with accessibility needs, I want the website to be accessible, with features like alt text for images and keyboard navigation, to ensure a positive experience for all users.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/19)|
|As a Site User, I can click on the About link so that I can read about the site.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/20)|
|As a Site Admin, I can create or update the about page content so that it is available on the site.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/21)|
|As a Site User, I can click on a username link so that I can read about the user and see their posts.|Good.|[link](https://github.com/0davidog/Umbra-Report/issues/22)|


## Compatibility and Responsive Testing

<em>[As a Site User, I want the blog website to be responsive, ensuring a seamless experience on various devices, including desktops, tablets, and smartphones.](https://github.com/0davidog/Umbra-Report/issues/18)</em>

### Windows laptop

This project was developed using a Windows laptop running Windows 10 and the site was viewed on three browsers.

|Browser|Dimensions|Screen|
|-------|----------|------|
|Chrome|1920x1080|[laptop-screen-01](https://github.com/0davidog/Umbra-Report/assets/135815736/b4c55f9a-988c-4f1f-b38f-4b4460dda4f6)|
|Firefox|1920x1080|[laptop-screen-02](https://github.com/0davidog/Umbra-Report/assets/135815736/37b529ab-1bc1-4969-ae9f-57dd59ec2bfc)|
|Edge|1920x1080|[laptop-screen-03](https://github.com/0davidog/Umbra-Report/assets/135815736/369fa204-208d-4363-9bd3-0b3cd810c155)|


### Chrome Emulated Device Dimensions

|Device Name|Dimensions|Screen|
|-----------|----------|------|
|iPhoneSE|375x667|[chrome-screen-01](https://github.com/0davidog/Umbra-Report/assets/135815736/1724b0a9-6205-48dc-91d5-6e37ae192816)|
|iPhone XR|414x896|[chrome-screen-02](https://github.com/0davidog/Umbra-Report/assets/135815736/18515c06-9fc1-4bb1-ab7d-9d5eb5129f42)|
|iPhone 12 Pro|390x884|[chrome-screen-03](https://github.com/0davidog/Umbra-Report/assets/135815736/df78c75e-526c-4eec-9199-69d0792caebb)|
|iPhone 14 Pro Max|430x932|[chrome-screen-04](https://github.com/0davidog/Umbra-Report/assets/135815736/7d828914-94b9-4f97-a0c9-feccc0335a7d)|
|Pixel 7|412x915|[chrome-screen-05](https://github.com/0davidog/Umbra-Report/assets/135815736/8cad6e39-3718-418b-9162-375f71784214)|
|Samsung Galaxy S8+|360x740|[chrome-screen-06](https://github.com/0davidog/Umbra-Report/assets/135815736/13a88f06-4314-4070-89f6-ec1983438991)|
|Samsung Galaxy S20 Ultra|412x915|[chrome-screen-07](https://github.com/0davidog/Umbra-Report/assets/135815736/cf85a018-7e1d-4e0e-a80e-25dfab7486f5)|
|iPad Mini|768x1024|[chrome-screen-08](https://github.com/0davidog/Umbra-Report/assets/135815736/056730e0-1b87-4c9e-af22-05b1674b78fa)|
|iPad Air|820x1180|[chrome-screen-09](https://github.com/0davidog/Umbra-Report/assets/135815736/441e0ddb-df52-4b98-8f40-6d097dea1711)|
|iPad Pro|1024x1366|[chrome-screen-10](https://github.com/0davidog/Umbra-Report/assets/135815736/6cfa865e-cd53-4923-b077-4ba9223e2924)|
|Surface Pro 7|912x1368|[chrome-screen-11](https://github.com/0davidog/Umbra-Report/assets/135815736/178de9bf-2bb0-4222-b0a8-1f7320b0c67b)|
|Surface Duo|540x720|[chrome-screen-12](https://github.com/0davidog/Umbra-Report/assets/135815736/7b0dcdb7-dc3c-495e-b843-1766ef2f32b8)|
|Galaxy Fold|280x653|[chrome-screen-13](https://github.com/0davidog/Umbra-Report/assets/135815736/b7e74160-e214-441d-ad86-d6b369baf331)|
|Asus Zenbook Fold|853x1280|[chrome-screen-14](https://github.com/0davidog/Umbra-Report/assets/135815736/7d9cd5bc-5560-478d-8224-dd2f565505c2)|
|Samsung Galaxy A51/71|412x914|[chrome-screen-15](https://github.com/0davidog/Umbra-Report/assets/135815736/be0e69c7-615d-4df7-aef3-0750dfcfe20c)|
|Nest Hub|1024x600|[chrome-screen-16](https://github.com/0davidog/Umbra-Report/assets/135815736/d4e0a3c8-2689-41d0-b4be-032b0f6b2840)|
|Nest Hub Max|1280x800|[chrome-screen-17](https://github.com/0davidog/Umbra-Report/assets/135815736/bc640790-70ee-477d-8ca4-567cfa37f297)|

### Browserstack Devices

[Browserstack.com](https://www.browserstack.com/)

|Device|OS|Browser|Viewport|Screen|
|------|--|-------|--------|------|
|iPhone 14 Pro|IOS, v16.3|Chrome|390x664|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/9a12d5c5-1cba-4e22-91e6-b9844cc5bcca)|
|iPhone 13|IOS, v15.4|Safari|390x664|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/fbbe23ea-a94e-46ff-a9c2-d08ea91a6210)|
|Samsung Galaxy S23|Android, v13.0|Chrome|393x786|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/b8205eff-d57b-432a-b306-5e0ba3dbb923)|
|Samsung Galaxy S22|Android, v12.0|Chrome|360x649|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/1f8b10f7-8877-4ed6-83c0-b528afef054b)|
|Xiaomi Redmi Note 12|Android, v13.0|Chrome|393x736|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/45565893-957c-4dce-ba08-11730015b7d7)|
|iPad 9th|IOS, v15.3|Safari|810x1010|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/800f5958-84a6-4824-b02d-fa23600c32be)|
|Mac Ventura|?|Safari|1920x927|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/163a7cef-9bb7-44c5-a872-886025d76eee)|
|iPhone XS|IOS, v15.3|Safari|375x635|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/61527504-b178-4aac-8f36-bb94df446615)|

### Market Share insights

I used [statcounter.com](https://gs.statcounter.com/) to give me an idea of which devices, browsers and operating systems I should focus on due to their popularity.

|Data|Image|
|----|-----|
|Desktop Browser Market Share:|![StatCounter-browser-ww-monthly-202302-202402-bar](https://github.com/0davidog/Umbra-Report/assets/135815736/c0e4e1ed-5d88-4c80-92cf-383cc677a3d1)|
|Mobile Browser Market Share:|![StatCounter-browser-ww-monthly-202302-202402-bar(1)](https://github.com/0davidog/Umbra-Report/assets/135815736/cb498dbd-56e2-4da1-ad78-203a71ad6bf3)|
|Mobile Vendor Market Share:|![StatCounter-vendor-ww-monthly-202302-202402-bar](https://github.com/0davidog/Umbra-Report/assets/135815736/5875661b-d524-43c0-8bcd-0f38362c1943)|
|Tablet Vendor Market Share:|![StatCounter-vendor-ww-monthly-202302-202402-bar(1)](https://github.com/0davidog/Umbra-Report/assets/135815736/b0d93449-afeb-4e58-aa4f-fcd2cd5a688c)|
|Operating System Market Share:|![StatCounter-os_combined-ww-monthly-202302-202402-bar](https://github.com/0davidog/Umbra-Report/assets/135815736/2aaf24a7-9c43-41d3-846c-04f390ee5d5d)|

## Accessibility Testing

<em>[As a Site User with accessibility needs, I want the website to be accessible, with features like alt text for images and keyboard navigation, to ensure a positive experience for all users.](https://github.com/0davidog/Umbra-Report/issues/19)</em>

### Accessibility Audits

#### Performance, Accessibility, Best Practices and SEO

[PageSpeed Insights](https://pagespeed.web.dev/) was used to audit the site's features for performance, accessibility, best practices and SEO. This was recommended as a more accurate reading than Chrome's lighthouse tool. The site scored 100 throughout on accessibly, best practice and SEO, which is good. Performance wise, the site runs much better on desktop than it does mobile. For a better performance on mobile, time could be taken to look in to optimising Cumulative Layout Shift, First Contentful Paint and largest Contentful Paint.

|Page|Factor|Performance|Accessibility|Best Practices|SEO|Screen Capture|
|----|------|-----------|-------------|--------------|---|--------------|
|[Index](https://umbra-report-f975c52ec09c.herokuapp.com/)|Mobile|82|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/045d9c6b-6060-4166-b011-2740133d1949)|
|[Index](https://umbra-report-f975c52ec09c.herokuapp.com/)|Desktop|92|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/e8ef7cd7-3b7f-46b0-b4c6-ddab770a94a7)|
|[About](https://umbra-report-f975c52ec09c.herokuapp.com/about/)|Mobile|59|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/3aea895a-322a-442a-b33f-34c2b42864a6)|
|[About](https://umbra-report-f975c52ec09c.herokuapp.com/about/)|Desktop|92|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/5db3899e-2d6b-4343-8342-acda94048bac)|
|[User01](https://umbra-report-f975c52ec09c.herokuapp.com/profile/0davidog/)|Mobile|75|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/892ffa8f-5af4-4f71-9202-656969914417)|
|[User01](https://umbra-report-f975c52ec09c.herokuapp.com/profile/0davidog/)|Desktop|93|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/71ebb3ab-ea1a-4414-8e3b-4906d250990b)|
|[Report01](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/)|Mobile|86|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/26f7daca-d88c-4caa-9518-68973e7f666d)|
|[Report01](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/)|Desktop|93|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/98a92890-f589-4c03-8deb-112e113f143a)|
|[Report02](https://umbra-report-f975c52ec09c.herokuapp.com/bermuda3/)|Mobile|84|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/081cf1c8-87f7-41a5-a759-119b732396d8)|
|[Report02](https://umbra-report-f975c52ec09c.herokuapp.com/bermuda3/)|Desktop|98|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/3ea27599-f396-4253-9218-961fcdc3fe2d)|
|[CreateReport](https://umbra-report-f975c52ec09c.herokuapp.com/create/)|Mobile|86|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/882f6853-6999-45e5-a0bd-7a626d07a479)|
|[CreateReport](https://umbra-report-f975c52ec09c.herokuapp.com/create/)|Desktop|98|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/4c2d4196-e41d-46cb-a95c-b94924281179)|
|[EditReport](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/edit/)|Mobile|87|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/0ec59303-43ae-4e1b-8634-fcb8ea8c820d)|
|[EditReport](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/edit/)|Desktop|95|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/734c2da0-a02a-4894-8684-ddf7ee548826)|
|[SignUp](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/signup/)|Mobile|77|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/efd7930d-1330-480b-aa83-3e8bb31b7016)|
|[SignUp](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/signup/)|Desktop|93|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/dc715fcb-5c7b-4a9f-aba1-bddbacc2ea7f)|
|[Login](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/login/)|Mobile|82|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/f461eaa8-9b91-438b-a99a-bd55706e88f0)|
|[Login](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/login/)|Desktop|99|100|100|100|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/341019ab-33e5-4944-8ed7-623068088e2c)|

[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) Was used to check for errors and contrast errors throughout the site.

|Page|Result|Screen Capture|
|----|------|--------------|
|[Index](https://umbra-report-f975c52ec09c.herokuapp.com/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/dd54599a-6eb9-4051-a06b-efbdf160ebe4)|
|[About](https://umbra-report-f975c52ec09c.herokuapp.com/about/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/e962c098-8af2-4253-bd61-6866917e7df3)|
|[User01](https://umbra-report-f975c52ec09c.herokuapp.com/profile/0davidog/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/19b19792-0b69-49ab-a5ab-c998ff2b391b)|
|[User02](https://umbra-report-f975c52ec09c.herokuapp.com/profile/Nosferatu302/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/9162a676-5ca0-412c-a0e0-703422830c86)|
|[Report01](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/9253555a-e5ab-4b7b-999c-80aff5701a5e)|
|[Report02](https://umbra-report-f975c52ec09c.herokuapp.com/bermuda3/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/c5111f12-58f9-4390-ba2d-96f3d10fd2bb)|
|[CreateReport](https://umbra-report-f975c52ec09c.herokuapp.com/create/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/8e03efe8-56ee-436a-b480-c0ba88d849f5)|
|[EditReport](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/edit/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/71293a8d-d5b4-4139-b4a4-b33f3046d8a1)|
|[SignUp](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/signup/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/bfa7d083-724c-46d2-ac9c-d89557f45d92)|
|[Login](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/login/)|No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/f583861b-d25e-400e-995e-018bbe5f9ae5)|
|[404](https://umbra-report-f975c52ec09c.herokuapp.com/404/)| No errors.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/ce0518df-caaf-4786-a70c-0daf434d5c1d)|

### Keyboard Navigation

Using a reference from [https://webaim.org](https://webaim.org/techniques/keyboard/#testing) I tested the keyboard navigation options that were relevant to the site (side scrolling or radio inputs couldn't be tested for example as they're not utilised on the site).

- [x] Tab key navigates forward to interactive elements.
- [x] Shift+Tab navigates backward to interactive elements.
- [x] Enter key activates links.
- [x] Enter or Spacebar activate buttons.
- [x] ↑/↓ - navigate between dropdown menu options.
- [x] Spacebar expands dropdown menu options.
- [x] Enter/Esc select dropdown menu option and collapse.
- [x] Typing letters jumps to a dropdown menu option.
- [x] Esc button closes modal dialogue box.
- [x] ↑/↓ buttons scroll vertically
- [x] Spacebar/Shift + Spacebar scroll by page (no button in focus).

## Validation Testing

### CSS Validation

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code through direct input.

|Result|Screen Capture|
|------|--------------|
|No Error Found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/b962aa9c-223b-4f2d-8c4d-6629ff71bd91)|

### HTML Validation

[W3C  Markup Validation Service](https://validator.w3.org/) was used to validate the html through direct code input. The html was acquired for each page by viewing the page source code on the deployed site.

|Page|Result|Screen Capture|
|----|------|--------------|
|[Index](https://umbra-report-f975c52ec09c.herokuapp.com/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/3a002a03-5be4-4678-b8e2-b7f30cbef0eb)|
|[About](https://umbra-report-f975c52ec09c.herokuapp.com/about/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/01018cc3-95ac-4d3e-ae6f-87b969c6fffd)|
|[User01](https://umbra-report-f975c52ec09c.herokuapp.com/profile/0davidog/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/58d33ad5-f7e9-41fb-8c76-ccd935281961)|
|[User02](https://umbra-report-f975c52ec09c.herokuapp.com/profile/Nosferatu302/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/a568860f-54e9-42d5-8e9a-9001befcb995)|
|[Report01](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/b89e429e-d66d-4f0d-b004-1bc0a110fa26)|
|[Report02](https://umbra-report-f975c52ec09c.herokuapp.com/bermuda3/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/cccd8064-d3b3-4327-b591-e1d6b9b4630f)|
|[CreateReport](https://umbra-report-f975c52ec09c.herokuapp.com/create/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/62c24ec0-bd04-4917-a23b-1f27ef331e23)|
|[EditReport](https://umbra-report-f975c52ec09c.herokuapp.com/noises-in-the-loft/edit/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/1386e7b6-731e-4b5d-a50a-f7ad6dcd014e)|
|[SignUp](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/signup/)|4 errors. * |[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/28ab4d89-9646-4853-b006-7c74e2ef400e)|
|[Login](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/login/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/ac4b0230-3554-4d5d-8b4f-e6ff24dcc90d)|
|[Logout](https://umbra-report-f975c52ec09c.herokuapp.com/accounts/logout/)|No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/bb469d00-1ce3-4f47-8722-80269e868760)|
|[404](https://umbra-report-f975c52ec09c.herokuapp.com/404/)| No errors or warnings to show.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/a5598dab-1566-4ea2-97ea-94d353f2249e)|

* The 4 errors listed on the sign up page come from external html code that I don't have access to, so they are ignored for the time being.

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the two javascript files through direct input of code.

`/*jshint esversion: 6 */` Was added to the test to remove ES6 warnings.

`import * as bootstrap from 'bootstrap';` Was also added to the test to remove an udefinded variable error (if included in app code this line breaks modal function).

|File|Result|Screen Capture|
|----|------|--------------|
|comment.js|No error found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/42dbef17-beae-462b-9e22-f7faff12ccad)|
|delete_report.js|No error found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/15803d9b-79dd-424c-88ae-44d7e83dbe9f)|

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the relevant python files through direct input of code.

|File|Result|Screen Capture|
|----|------|--------------|
|umbra/urls.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/fae49a9e-873e-4831-98f9-abe2dc17a7cf)|
|blog/admin.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/4ef16586-cfd7-4029-8dc3-58ed3051f1b4)|
|blog/forms.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/f6ead999-65bd-467f-9bfe-652605c24271)|
|blog/models.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/8ea7317d-a3b4-407d-82a7-f79e7125ef77)|
|blog/urls.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/4c70200d-de4b-4296-b93d-ad36872cfd58)|
|blog/views.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/a2543ba0-da00-4fc9-a5af-9bbbf94ceb88)|
|blog/test_views.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/c0ba7c55-da3b-4886-ade0-b47fe0186a70)|
|blog/test_forms.py|No errors found.|[Screen](https://github.com/0davidog/Umbra-Report/assets/135815736/064be549-f207-4ca6-a813-36282ee680ce)|

## Automated Testing

As time was short, the automated testing done on this project was small and very basic. The Code Institute walkthought project 'I Think, Therfore I Blog" informed the initial tests while the TestHomePage unit test was inspired by django documentation on automated tests [(here)](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#example).

[test_forms.py](https://github.com/0davidog/Umbra-Report/blob/main/blog/test_forms.py) Contains two TestCase classes: TestReportForm and TestCommentForm.

The TestReportForm class features two methods.

- test_report_form_is_valid() Method: This method tests whether the form is valid when all required fields are properly filled. It creates an instance of ReportForm with sample data (a title, a category, some content, and a status), and then checks if the form is valid using assertTrue() assertion. If the form is valid, the test passes; otherwise, it fails.
- test_empty_report_form_is_invalid() Method: This method tests whether the form is invalid when all required fields are empty. It creates another instance of ReportForm with empty values for all fields and checks if the form is valid using assertFalse() assertion. If the form is invalid (as it should be when all required fields are empty), the test passes; otherwise, it fails.

The TestCommentForm class features two methods.

- test_comment_form_is_valid() Method: This method tests whether the form is valid when the required field (content) is filled with some text. It creates an instance of CommentForm with a sample comment content and then checks if the form is valid using the assertTrue() assertion. If the form is valid, the test passes.
- test_empty_comment_form_is_valid() Method: Similarly, this method tests whether the form is valid when the required field (content) is left empty. It creates another instance of CommentForm with an empty value for the content field and then checks if the form is valid using the assertFalse() assertion. If the form is invalid (as it should be when the required field is empty), the test passes.

[test_views](https://github.com/0davidog/Umbra-Report/blob/main/blog/test_views.py) Contains two TestCase classes: TestFullReportView and TestHomePage.

The TestFullReportView class features three methods:

- setUp() Method: This method is part of the TestCase class and is used for test setup. In this case, it creates a superuser using create_superuser() method from Django's User model, and it also creates a report (Report model instance) associated with this user. The report contains various fields like title, author, slug, description, content, status, and category. This setup ensures that there's data available for testing the view.
- test_render_full_report_page_with_comment_form() Method: This method tests whether the full report page is rendered correctly along with the comment form. It sends a GET request to the view responsible for displaying a full report page (full_report view) using self.client.get(). Then it asserts that the response status code is 200 (indicating success), and it checks whether the response contains the title and content of the report. Additionally, it verifies that the context of the response contains an instance of the CommentForm.
- test_comment_submission() Method: This method tests the functionality of submitting a comment on a report. First, it logs in as the superuser created in the setUp() method using self.client.login(). Then it creates a POST request with comment data and sends it to the view associated with the full report page (full_report view). Afterward, it asserts that the response status code is 200 and checks whether the response contains a specific message indicating that the comment has been submitted and is awaiting approval.

The TestHomePage class features three methods:

- setUp() Method: This method is used for test setup. In this case, it creates a request factory instance (RequestFactory) and creates a superuser using create_superuser() method from Django's User model. This setup ensures that there's a user available for testing authentication-related behavior.
- test_index_page_view() Method: This method tests various aspects of the home page view. It does the following:
  - Creates a GET request to the root URL ('/') using the request factory.
  - Verifies that the default template used by the view is 'base.html'.
  - Calls the home page view (ReportList.as_view()) with the created request.
  - Checks if certain text and navigation links are present in the response content, both for an unauthenticated user and for an authenticated user (superuser in this case).
  - Verifies that certain admin links are absent for unauthenticated users and present for authenticated users.
- test_404_view() Method: This method tests whether the 404 error page is displayed when a nonexistent URL is requested. It creates a GET request to a nonexistent URL ('/thispageisnowhere/') and checks whether the '404.html' template is used in the response.

## Defects

- Once I had decided to keep the image widths uniform to assist with page performance, I had caused an issue in which images smaller than 500px in width were distorted. This was an easy fix and just required `object-fit: contain;` to be placed in the CSS.
- A contrast issue was detected in the red colour (#800000) used for headings and links. This was missed as it did not appear in the WAVE or PageSpeed audits detailed in this document. The issue however could be seen when inspecting an element in Chrome's dev tools and viewing the contrast score. Chrome's suggested colour instead was (#BA0000) so I switched to this shade. With this in mind, I checked the grey colour used (#808080) and followed Chrome's suggestion to switch to a slightly lighter shade of grey (#969696).

## Defects of Note

Comment edits were failing to update. 

This was due to the url expecting a trailing slash: 

```
path(
    '<slug:slug>/delete_comment/<int:comment_id>/',
    views.comment_delete,
    name='comment_delete'
    ),
```

but the JS was missing one:

```
commentForm.setAttribute("action", `edit_comment/${commentId}`);
```

So a trailing slash was added to fix:

```
commentForm.setAttribute("action", `edit_comment/${commentId}`);
```

## Outstanding Defects

No known defects outstanding.
