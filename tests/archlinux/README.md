## Arch Linux Docker test image

This folder provides a small **Arch Linux** Docker image intended as an **interactive sandbox**.
It copies the `awesome-os-setup/` repo into the container user's home so you can jump in and run the setup manually.

### Build

From the `awesome-os-setup/` directory:

```bash
docker build -f tests/archlinux/Dockerfile -t awesome-os-setup-arch-test .
```

### Run (interactive)

```bash
docker run --rm -it awesome-os-setup-arch-test
```

This drops you into `bash` in:

- `/home/tester/awesome-os-setup`

From there you can try your normal workflow, for example:

```bash
make install
make run
```

