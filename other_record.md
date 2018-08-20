- **安装IJulia的时候，其中一个ZMQ始终无法下载，如何本地安装？**

```julia
Pkg.build("IJulia")
  Building Conda ──→ `~/.julia/packages/Conda/m7vem/deps/build.log`
  Building ZMQ ────→ `~/.julia/packages/ZMQ/yClfT/deps/build.log`
┌ Error: Error building `ZMQ`:
│ ┌ Warning: Could not extract the platform key of https://github.com/JuliaInterop/ZMQBuilder/releases/download/v4.2.5+6/ZMQ.x86_64-apple-darwin14.tar.gz; continuing...
```

*下载包`https://github.com/JuliaInterop/ZMQBuilder/releases/download/v4.2.5+6/ZMQ.x86_64-apple-darwin14.tar.gz`到`~/.julia/packages/ZMQ/yClfT/deps/usr/downloads`下，在直接运行`Pkg.build("ZMQ")`*