const numParticipants = prompt("How many participants?");

const participants = [];

for (let i = 0; i < numParticipants; i++) {
  const name = prompt(`Enter the name of participant ${i + 1}:`);
  participants.push(name);
}

participants.sort();

console.log("Participants in alphabetical order:");
participants.forEach(name => console.log(name));