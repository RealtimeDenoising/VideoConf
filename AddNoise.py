# p_salt = .05; %// probability of salt
# p_pepper = .01; %// probability of pepper
#
# if strcmp(class(img),'uint8')
#     salt_value = uint8(255);
# else
#     salt_value = 1;
# end
# pepper_value = 0;
#
# aux = rand(size(img)); %// generate random values
# img(aux<=p_salt) = salt_value;  %// add salt
# img((aux>p_salt) & (aux<=p_salt+p_pepper)) = pepper_value; %// add pepper
#
# imshow(img) %// show image