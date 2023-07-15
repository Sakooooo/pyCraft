with import <nixpkgs> {};

mkShell {
  name = "PyCraft - Nix Shell";
  nativeBuildInputs = [
    python3
  ];
  buildInputs = with python310Packages; [
    pygame
    pyopengl
    numpy
  ];

}
