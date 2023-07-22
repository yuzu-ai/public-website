# YuzuAI Public Website

## 🚀 Getting Started 

### 📦 Dependencies

- next 13.4+
- node v18+
- npm v9.5+
- tailwind v3.3+

### 👉 Development Command

```
yarn install
```

```
yarn run dev
```

### 👉 Build Command

```
yarn run build
```

### Update Your Profile

- Add your profile image to `public/images/` directory, remember the file name.
- Change url in `src/content/authors/` directory, the file name should be your name.
- If any information field is left blank, then it will not be displayed on the website.

### Blog Image

Blog image should be added to `public/images/blog` directory, remember the filepath. It's recommended to have a folder for each blog post to better file management. When invoke these images, format as follows:
```
![Image Title](/images/blog/post/image.png)
```