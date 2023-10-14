// Smart Contract Code (Solidity)
pragma solidity ^0.8.0;

contract WheelchairControl {
    address public user;
    bool public isMoving;

    modifier onlyUser() {
        require(msg.sender == user, "Only the user can control the wheelchair.");
        _;
    }

    function startMoving() external onlyUser {
        isMoving = true;
        emit MoveActorRequested(msg.sender, block.timestamp);
    }

    function stopMoving() external onlyUser {
        isMoving = false;
        emit MoveActorRequested(msg.sender, block.timestamp);
    }
}