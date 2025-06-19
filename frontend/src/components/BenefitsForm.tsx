import React from 'react';
import {
  Box,
  Button,
  Typography,
  FormGroup,
  FormControlLabel,
  Checkbox,
  TextField,
} from '@mui/material';

interface BenefitsFormProps {
  formData: any;
  setFormData: (data: any) => void;
  onNext: () => void;
  onBack: () => void;
}

const BenefitsForm: React.FC<BenefitsFormProps> = ({
  formData,
  setFormData,
  onNext,
  onBack,
}) => {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onNext();
  };

  const handleBenefitChange = (benefit: string) => {
    const newBenefits = formData.preferred_benefits.includes(benefit)
      ? formData.preferred_benefits.filter((b: string) => b !== benefit)
      : [...formData.preferred_benefits, benefit];
    setFormData({
      ...formData,
      preferred_benefits: newBenefits,
    });
  };

  const handleExistingCardsChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const cards = e.target.value.split(',').map((card) => card.trim());
    setFormData({
      ...formData,
      existing_cards: cards,
    });
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
      <Typography variant="h6" gutterBottom>
        What benefits are you looking for?
      </Typography>
      <FormGroup>
        <FormControlLabel
          control={
            <Checkbox
              checked={formData.preferred_benefits.includes('cashback')}
              onChange={() => handleBenefitChange('cashback')}
            />
          }
          label="Cashback Rewards"
        />
        <FormControlLabel
          control={
            <Checkbox
              checked={formData.preferred_benefits.includes('travel_points')}
              onChange={() => handleBenefitChange('travel_points')}
            />
          }
          label="Travel Points"
        />
        <FormControlLabel
          control={
            <Checkbox
              checked={formData.preferred_benefits.includes('lounge_access')}
              onChange={() => handleBenefitChange('lounge_access')}
            />
          }
          label="Airport Lounge Access"
        />
        <FormControlLabel
          control={
            <Checkbox
              checked={formData.preferred_benefits.includes('fuel_rewards')}
              onChange={() => handleBenefitChange('fuel_rewards')}
            />
          }
          label="Fuel Rewards"
        />
        <FormControlLabel
          control={
            <Checkbox
              checked={formData.preferred_benefits.includes('dining_rewards')}
              onChange={() => handleBenefitChange('dining_rewards')}
            />
          }
          label="Dining Rewards"
        />
      </FormGroup>
      <TextField
        fullWidth
        label="Existing Credit Cards (comma-separated)"
        value={formData.existing_cards.join(', ')}
        onChange={handleExistingCardsChange}
        margin="normal"
        helperText="List any credit cards you currently have"
      />
      <Box sx={{ mt: 3, display: 'flex', justifyContent: 'space-between' }}>
        <Button onClick={onBack}>Back</Button>
        <Button
          type="submit"
          variant="contained"
          color="primary"
          disabled={formData.preferred_benefits.length === 0}
        >
          Get Recommendations
        </Button>
      </Box>
    </Box>
  );
};

export default BenefitsForm; 