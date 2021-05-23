# example with code 
Add-Type -AssemblyName System.Speech
$synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer
# as in _____ and https://docs.microsoft.com/en-us/uwp/api/windows.media.speechsynthesis.speechsynthesizer?view=winrt-19041 
$synth.Speak('hello');
# test voice speaking 
for ($num = 1 ; $num -le 3 ; $num++ ) {
  sleep 300; $num3=$num*5; "$num3 minutes passed.. "; 
  $synth.Speak($num3) ; $synth.Speak('really') ; $synth.Speak($num3) ; $synth.Speak(' minutes elapsed!') 
} ; 
$synth.Speak('ohhh, yes!') ; $synth.Speak($num3) ; $synth.Speak(' minutes passed by, yes, be aware')
